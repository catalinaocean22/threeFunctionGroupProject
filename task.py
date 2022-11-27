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
    pass


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
