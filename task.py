import re

# dictionaries for conversions
CHAR_TO_DIGIT = {'0': 0,
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

DIGIT_TO_CHAR = {0: '0',
                 1: '1',
                 2: '2',
                 3: '3',
                 4: '4',
                 5: '5',
                 6: '6',
                 7: '7',
                 8: '8',
                 9: '9',
                 10: 'A',
                 11: 'B',
                 12: 'C',
                 13: 'D',
                 14: 'E',
                 15: 'F'
                 }


def conv_num_sign_handler(is_positive, return_val):
    return return_val if is_positive else return_val * -1


def conv_num(num_str):

    # If the input is not a string, is an empty string, contains multiple '.' characters,
    # or is an otherwise unacceptable string return None
    invalid_strings = ['-', '.', ' ']
    multiple_decimals = re.match(r"\.+.*\.+", num_str)
    if type(num_str) != str or len(num_str) == 0 or num_str in invalid_strings or multiple_decimals:
        return None

    # Use this to check if num_string is valid hex
    hex_regex = r"^-?(0x|0X)+[0-9a-fA-F]+$"
    if re.fullmatch(hex_regex, num_str):
        return_val = 0
        exponent = 0
        is_positive = True
        # Check if the number as negative, and remove the symbol if so
        if num_str[0] == '-':
            is_positive = False
            num_str = num_str[1:]

        # Remove the hex prefix and uppercase the string for case insensitivity
        num_str = num_str[2:].upper()

        # Iterate through the num_str backwards, increasing the exponent each time
        for hex in reversed(num_str):
            return_val = return_val + (CHAR_TO_DIGIT[hex] * 16 ** exponent)
            exponent += 1
        return conv_num_sign_handler(is_positive, return_val)

    # Use this to check if num_str is a valid number
    num_regex = r"^-?[0-9]*\.?[0-9]*$"
    # check if hex
    hex_regex = r"^-?(0x|0X)+[0-9a-fA-F]+$"
    if re.fullmatch(hex_regex, num_str):
        return conv_hex(num_str)

    # check if decimal
    num_regex = r"^-?[0-9]*\.?[0-9]*$"
    if re.fullmatch(num_regex, num_str):
        return_val = 0
        exponent = 0
        is_positive = True

        # Check if the number as negative, and remove the symbol if so
        if num_str[0] == '-':
            is_positive = False
            num_str = num_str[1:]

        # Iterate through the num_str backwards, increasing the exponent each time
        for num in reversed(num_str):
            if num == '.':
                return_val = return_val / 10 ** exponent
                exponent = 0
                continue
            return_val = return_val + (CHAR_TO_DIGIT[num]) * 10 ** exponent
            exponent += 1
        return conv_num_sign_handler(is_positive, return_val)
    # invalid input
    return None


def conv_hex(num_str):
    # setup
    return_val = 0
    exponent = 0
    positive = True

    # Check if the number is negative, and remove the symbol if so
    if num_str[0] == '-':
        positive = False
        num_str = num_str[1:]

    # Remove the hex prefix and uppercase the string for case insensitivity
    num_str = num_str[2:].upper()

    # Iterate through the num_str backwards,
    # increasing the exponent each time
    for hex_str in reversed(num_str):
        return_val = return_val + (CHAR_TO_DIGIT[hex_str] * 16 ** exponent)
        exponent += 1
    if positive:
        return return_val
    else:
        return return_val * -1


def conv_decimal(num_str):
    # setup
    return_val = 0
    exponent = 0
    positive = True

    # Check if the number is negative, and remove the symbol if so
    if num_str[0] == '-':
        positive = False
        num_str = num_str[1:]

    # Iterate through the num_str backwards,
    # increasing the exponent each time
    for num in reversed(num_str):
        if num == '.':
            return_val = return_val / 10 ** exponent
            exponent = 0
            continue
        return_val = return_val + (CHAR_TO_DIGIT[num]) * 10 ** exponent
        exponent += 1
    if positive:
        return return_val
    else:
        return return_val * -1


def my_datetime(num_sec):
    """
    Takes the passed integer as the total seconds and gives the date it represents
    The function first decides which of the three scenarios the given seconds falls in based on the year: a day before
    1972, a day on the year 1972, and a day after the year 1972
    """
    SEC_A_DAY = 86400
    year = 1970
    month = 1
    day_in_month = 1
    REG_DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    LEAP_DAYS_IN_MONTH = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = num_sec//SEC_A_DAY  # number of days the passed seconds represent before considering the leftover seconds
    DAYS_LEAP = 366
    DAYS_REG = 365
    DAY_SUM_BEFORE_1972 = DAYS_REG * 2  # a constant, sum of days of the two years 1970 and 1971 used to calculate the
    # result if the passed parameter falls on a day before 1972

    # If the passed seconds represent a day before 1972
    if days < DAY_SUM_BEFORE_1972:  # here if days is equal to DAY_SUM_BEFORE_1972, the year would be 1972 itself as
        # shown below this condition
        year = 1970 + (days//DAYS_REG)
        remaining_days = days - DAY_SUM_BEFORE_1972
        # using helper function get_my_date we can get the month, day, and year as integers
        month = get_my_date(num_sec, remaining_days, REG_DAYS_IN_MONTH, DAYS_REG, year)[0]
        day_in_month = get_my_date(num_sec, remaining_days, REG_DAYS_IN_MONTH, DAYS_REG, year)[1]

    # If the passed seconds represent a day on the year 1972, which is a leap year
    if DAY_SUM_BEFORE_1972 <= days < DAY_SUM_BEFORE_1972 + DAYS_LEAP:
        year = 1972
        remaining_days = days - DAY_SUM_BEFORE_1972
        # using helper function get_my_date we can get the month, day, and year as integers
        month = get_my_date(num_sec, remaining_days, LEAP_DAYS_IN_MONTH, DAYS_LEAP, year)[0]
        day_in_month = get_my_date(num_sec, remaining_days, LEAP_DAYS_IN_MONTH, DAYS_LEAP, year)[1]

    # If the passed seconds represent a day on the year 1972. This one includes some special cases which is handled
    # separately within the if condition
    if days >= DAY_SUM_BEFORE_1972 + DAYS_LEAP:
        year = 1972
        remain_days = days - (DAY_SUM_BEFORE_1972 + DAYS_LEAP)  # number of days after subtracting the days before 1972
        new_remain_days_and_year = get_my_year(remain_days, year, DAYS_REG, DAYS_LEAP)  # decides which year num_sec
        # falls in and get the updated remain_days
        remain_days = new_remain_days_and_year[0]
        year = new_remain_days_and_year[1]
        if remain_days >= 0:  # to handle cases where the actual year should be the next year
            year += 1
        # using helper function get_my_date we can get the month, day, and year as integers.
        if is_leap(year):  # if it's a leap year
            month = get_my_date(num_sec, remain_days, LEAP_DAYS_IN_MONTH, DAYS_LEAP, year)[0]
            day_in_month = get_my_date(num_sec, remain_days, LEAP_DAYS_IN_MONTH, DAYS_LEAP, year)[1]
        if not is_leap(year):  # if it's a regular year
            result = get_my_date(num_sec, remain_days, REG_DAYS_IN_MONTH, DAYS_REG, year)
            month = result[0]
            day_in_month = result[1]
            year = result[2]
    # This part we turn the integer results to strings before returning them.
    if month < 10:
        month = str(0) + str(month)
    if day_in_month < 10:
        day_in_month = str(0) + str(day_in_month)
    return str(month) + "-" + str(day_in_month) + "-" + str(year)


# this is the function to be used to replace the repeated code above
def get_my_date(num_sec, days_needed, month_list, days_in_year, year):
    """
    Helper function to get the month, day, and year based on num_sec shared by all three cases: before 1972, 1972,
    and after 1972. Currently not all cases need the year value, yet it's part of the parameters as this function is
    shared.
    some variables look the same as in my_datetime
    """
    sec_day = 86400
    month = 1
    day_in_month = 1
    total_days = month_list[0]  # a sum of number of days we've gone through on our way to reach to the current month
    days = num_sec // sec_day
    i = 0
    while i <= len(month_list) - 1:  # going through the months of the given year and handle different cases
        # This is to handle special cases for the last day of leap years where the year passed here is 1 year too many
        if not is_leap(year) and num_sec - days * sec_day < sec_day and abs(days_needed) == 366:
            year -= 1
        if days_needed % days_in_year > total_days:  # going through the months to subtract the days_needed and
            # accumulate total_days until we reach our target month
            day_in_month = (days_needed % days_in_year - total_days)
            month += 1
            total_days += month_list[i + 1]
            i += 1
        # One of the cases we arrive at the current month so we will figure out the day: there's a previous month
        elif month_list[i - 1] < days_needed % days_in_year < total_days:
            day_in_month = days_needed % days_in_year - (total_days - month_list[i]) + 1
            break
        # One of the cases we arrive at the current month so we will figure out the day: there's no previous month
        elif 0 < days_needed % days_in_year < total_days:
            day_in_month = days_needed % days_in_year + 1
            break
        elif days_needed % days_in_year == total_days:  # the first day of a month
            if num_sec >= days * sec_day:
                day_in_month = 1
                month += 1
            break
        elif days_needed == days_in_year:  # the first day of the year
            day_in_month = 1
            break
        else:
            break
    if num_sec == 0:  # for 01-01-1970
        day_in_month = 1
    return [month, day_in_month, year]


def get_my_year(days_left, my_year, days_reg, days_leap):
    """
    The helper function to get the year the day represented by the given seconds falls in
    :param days_left:
    :param my_year: the starting year for the while loop
    :param days_reg: the constant from my_datetime we simply pass here so we don't type 365 and 366
    :param days_leap: the constant from my_datetime we simply pass here so we don't type 365 and 366
    :return: the updated remaining days and updated year
    """
    while days_left >= days_reg:  # reduce the total remaining days year by year until we are (almost)
        # in the current year
        days_left -= days_reg
        my_year += 1
        if is_leap(my_year):  # when we encounter a leap year we reduce 366 (days_leap) instead of 365 days
            days_left -= days_leap
            my_year += 1
    return [days_left, my_year]


def is_leap(year):
    """to decide if a year is a leap year"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def conv_endian(num, endian='big'):
    # validate
    if endian not in ['big', 'little']:
        return None
    is_negative = num < 0
    num = abs(num)

    # calculate remainders
    remainders = []
    while num > 0:
        remainders.append(num % 16)
        num //= 16
    if len(remainders) % 2 == 1:
        # to form bytes, need pairs of base-16
        remainders.append(0)

    # build byte_strings
    byte_strings = []
    while remainders:
        byte_strings.append("".join([DIGIT_TO_CHAR[remainders.pop()],
                                     DIGIT_TO_CHAR[remainders.pop()]]))
    if endian == 'little':
        byte_strings.reverse()

    # build result
    result = " ".join(byte_strings)
    if is_negative:
        result = "-" + result
    return result
