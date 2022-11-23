import re


def conv_num(num_str):

    # If the input is not a string, is an empty string, or contains multiple '.' characters, return None
    multiple_decimals = re.match(r"\.+.*\.+", num_str)
    if type(num_str) != str or len(num_str) == 0 or multiple_decimals:
        return None

    # Use this to check if num_string is valid hex
    hex_regex = r"^-?(0x|0X)+[0-9a-fA-F]+$"
    if re.fullmatch(hex_regex, num_str):
        return_val = 0
        negative = False
        if num_str[0] == '-':
            negative = True
            num_str = num_str[1:]
        num_str = num_str[2:].upper()
        exponent = 0
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
        for hex in reversed(num_str):
            return_val = return_val + (hex_dict[hex] * 16 ** exponent)
            exponent += 1
        if negative:
            return_val *= -1
        return return_val

    int_regex = r"^-?[0-9]+$"
    float_regex = r"^-?[0-9]+\.[0-9]+"

    if re.fullmatch(int_regex, num_str):
        return int(num_str)

    if re.fullmatch(float_regex, num_str):
        return float(num_str)

    return None


def my_datetime(num_sec):
    pass


def conv_endian(num, endian='big'):
    pass
