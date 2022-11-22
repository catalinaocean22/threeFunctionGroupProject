import re


def conv_num(num_str):

    # If the input is not a string, is an empty string, or contains multiple '.' characters, return None
    multiple_decimals = re.match(r"\.+.*\.+", num_str)
    if type(num_str) != str or len(num_str) == 0 or multiple_decimals:
        return None

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
