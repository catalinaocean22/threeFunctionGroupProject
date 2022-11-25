import re


def conv_num(num_str):

    # If the input is not a string, is an empty string, or contains multiple '.' characters, return None
    multiple_decimals = re.match(r"\.+.*\.+", num_str)
    if type(num_str) != str or len(num_str) == 0 or multiple_decimals:
        return None

    # Dict to convert the string values to their numeric values
    hex_dict = {'0': 0,
                '1': 1,
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9,
                'A': 10,
                'B': 11,
                'C': 12,
                'D': 13,
                'E': 14,
                'F': 15
                }

    # Use this to check if num_string is valid hex
    hex_regex = r"^-?(0x|0X)+[0-9a-fA-F]+$"
    if re.fullmatch(hex_regex, num_str):
        return_val = 0
        exponent = 0
        positive = True
        # Check if the number as negative, and remove the symbol if so
        if num_str[0] == '-':
            positive = False
            num_str = num_str[1:]

        # Remove the hex prefix and uppercase the string for case insensitivity
        num_str = num_str[2:].upper()

        # Iterate through the num_str backwards, increasing the exponent each time
        for hex in reversed(num_str):
            return_val = return_val + (hex_dict[hex] * 16 ** exponent)
            exponent += 1
        if positive:
            return return_val
        else:
            return return_val * -1

    # Use this to check if num_str is a valid number
    num_regex = r"^-?[0-9]*\.?[0-9]*$"

    if re.fullmatch(num_regex, num_str):
        return_val = 0
        exponent = 0
        positive = True

        # Check if the number as negative, and remove the symbol if so
        if num_str[0] == '-':
            positive = False
            num_str = num_str[1:]

        # Iterate through the num_str backwards, increasing the exponent each time
        for num in reversed(num_str):
            if num == '.':
                return_val = return_val / 10 ** exponent
                exponent = 0
                continue
            return_val = return_val + (hex_dict[num]) * 10 ** exponent
            exponent += 1
        if positive:
            return return_val
        else:
            return return_val * -1
    return None


def my_datetime(num_sec):
    def my_datetime(num_sec):
    sec_day = 86400
    year = 1970
    month = 1
    date = 1
    reg_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap_days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = num_sec//sec_day
    days_leap = 366
    days_reg = 365
    print(days)
    day_sum_before_1972 = days_reg * 2
    if days < day_sum_before_1972:
        year = 1970 + (days//365)
        total_days = reg_days_in_month[0]
        i = 0
        while i <= len(reg_days_in_month)-1:
            if days % 365 > total_days:
                date = (days % 365 - total_days)
                month += 1
                total_days += reg_days_in_month[i+1]
                i += 1
            elif reg_days_in_month[i - 1] < days % 365 < total_days:

                date = days % 365 - reg_days_in_month[i - 1] + 1
                break
            elif days % 365 == total_days:
                if num_sec > days * sec_day:
                    date = 1
                    month += 1
                break

            elif days % 365 == 0:
                date = 1
                break
            else:
                break

        if num_sec == 0:
            date = 1
        if num_sec % 86400 == 0 and num_sec != 0 and days % days_reg != 0 and date < reg_days_in_month[
                month - 1]:
            if date + 1 <= reg_days_in_month[month-1]:
                date += 1
            elif date + 1 > reg_days_in_month[month-1]:
                month += 1
                date = 1
        if num_sec > (days + 1) * 86400:
            if date + 1 <= reg_days_in_month[month-1]:
                date += 1
            elif date + 1 > reg_days_in_month[month-1]:
                month += 1
                date = 1

    # 1972
    if day_sum_before_1972 <= days < day_sum_before_1972 + days_leap:
        year = 1972
        total_days = leap_days_in_month[0]
        remaining_days = days - day_sum_before_1972
        i = 0
        while i <= len(leap_days_in_month) - 1:
            if remaining_days > total_days:
                date = (remaining_days - total_days)
                month += 1
                total_days += leap_days_in_month[i + 1]
                i += 1
            elif total_days - leap_days_in_month[i] < remaining_days < total_days:

                date = remaining_days - (total_days - leap_days_in_month[i])
                break
            elif remaining_days == total_days:
                if num_sec > days * sec_day:
                    date = 1
                    month += 1
                break
            elif days % days_reg == 0:
                date = 1
                break
            else:

                break

        if num_sec == 0:
            date = 1
        if num_sec % 86400 == 0 and num_sec != 0 and remaining_days % days_leap != 0 and date <= \
                leap_days_in_month[month - 1]:
            if date + 1 <= leap_days_in_month[month - 1]:
                date += 1
            elif date + 1 > leap_days_in_month[month - 1]:
                month += 1
                date = 1
        elif num_sec > (days + 1) * 86400:
            if date + 1 <= leap_days_in_month[month - 1]:
                date += 1
            elif date + 1 > leap_days_in_month[month - 1]:
                month += 1
                date = 1

    # after 1972
    if days >= day_sum_before_1972 + days_leap:
        year = 1972
        remain_days = days - (day_sum_before_1972 + days_leap)
        while remain_days >= days_leap:
            remain_days -= days_reg

            year += 1
            if is_leap(year):
                remain_days -= days_leap
                year += 1
        year += 1

        if is_leap(year):
            total_days = leap_days_in_month[0]
            i = 0
            while i <= len(leap_days_in_month) - 1:
                if remain_days > total_days:
                    date = (remain_days - total_days)
                    month += 1
                    total_days += leap_days_in_month[i + 1]
                    i += 1
                elif total_days - leap_days_in_month[i-1] < remain_days < total_days:

                    date = remain_days - (total_days - leap_days_in_month[i]) + 1
                    break
                elif remain_days == total_days:
                    if num_sec > days * sec_day:
                        date = 1
                        month += 1
                    break

                else:

                    break

            if num_sec == 0:
                date = 1
            if num_sec % 86400 == 0 and num_sec != 0 and remain_days % days_leap != 0 and date < \
                    leap_days_in_month[month-1]:
                if date + 1 <= leap_days_in_month[month - 1]:
                    date += 1
                elif date + 1 > leap_days_in_month[month - 1]:
                    month += 1
                    date = 1
            elif num_sec > (days + 1) * 86400:
                if date + 1 <= leap_days_in_month[month - 1]:
                    date += 1
                elif date + 1 > leap_days_in_month[month - 1]:
                    month += 1
                    date = 1

        if not is_leap(year):
            total_days = reg_days_in_month[0]
            i = 0
            while i <= len(reg_days_in_month) - 1:
                if remain_days > total_days:
                    date = (remain_days - total_days)
                    month += 1
                    total_days += reg_days_in_month[i + 1]
                    i += 1
                elif reg_days_in_month[i - 1] < remain_days < total_days:

                    date = remain_days - (total_days - reg_days_in_month[i]) + 1
                    break
                elif remain_days == total_days:
                    if num_sec > days * sec_day:
                        date = 1
                        month += 1
                    break
                elif remain_days % days_reg == 0:
                    date = 1
                    break
                else:
                    break
            if num_sec == 0:
                date = 1
            if num_sec % 86400 == 0 and num_sec != 0 and remain_days != 0 and date < reg_days_in_month[month-1]:
                if date + 1 <= reg_days_in_month[month - 1]:
                    date += 1
                elif date + 1 > reg_days_in_month[month - 1]:
                    month += 1
                    date = 1
            elif num_sec > (days + 1) * 86400:
                if date + 1 <= reg_days_in_month[month - 1]:
                    date += 1
                elif date + 1 > reg_days_in_month[month - 1]:
                    month += 1
                    date = 1

    if month < 10:
        month = str(0) + str(month)
    if date < 10:
        date = str(0) + str(date)
    return str(month) + "-" + str(date) + "-" + str(year)

# this is the function to be used to replace the repeated code above


"""
def get_data(num_sec, days_needed, month_list):
    month = 1
    date = 1
    total_days = month_list[0]
    days = num_sec // 86400
    i = 0
    while i <= len(month_list) - 1:
        if days_needed > total_days:
            date = (days_needed - total_days)
            month += 1
            total_days += month_list[i + 1]
            i += 1
        elif total_days - month_list[i] < days_needed < total_days:

            date = days_needed - (total_days - month_list[i])
            break
        elif days_needed == total_days:
            if num_sec > days * 86400:
                date = 1
                month += 1
            break
        elif days % 365 == 0:
            date = 1
            break
        else:

            break

    if num_sec == 0:
        date = 1
    if num_sec % 86400 == 0 and num_sec != 0 and days_needed != 0 and date < \
            month_list[month - 1]:
        if date + 1 <= month_list[month - 1]:
            date += 1
        elif date + 1 > month_list[month - 1]:
            month += 1
            date = 1
    elif num_sec > (days + 1) * 86400:
        if date + 1 <= month_list[month - 1]:
            date += 1
        elif date + 1 > month_list[month - 1]:
            month += 1
            date = 1
    return [month, date]
"""


def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    pass


def conv_endian(num, endian='big'):
    pass
