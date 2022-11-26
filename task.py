import re

char_to_digit = {'0': 0,
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
            return_val = return_val + (char_to_digit[hex] * 16 ** exponent)
            exponent += 1
        return conv_num_sign_handler(is_positive, return_val)

    # Use this to check if num_str is a valid number
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
            return_val = return_val + (char_to_digit[num]) * 10 ** exponent
            exponent += 1
        return conv_num_sign_handler(is_positive, return_val)
    return None


def my_datetime(num_sec):
    pass


def conv_endian(num, endian='big'):
    pass
