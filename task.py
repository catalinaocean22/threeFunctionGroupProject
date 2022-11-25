import re

# dictionaries for conversions
char_to_digit = { '0': 0,
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

digit_to_char = {  0:  '0',
                   1:  '1',
                   2:  '2',
                   3:  '3',
                   4:  '4',
                   5:  '5',
                   6:  '6',
                   7:  '7',
                   8:  '8',
                   9:  '9',
                   10: 'A',
                   11: 'B',
                   12: 'C',
                   13: 'D',
                   14: 'E',
                   15: 'F'
                }

def conv_num(num_str):

    # If the input is not a string, is an empty string, or contains multiple '.' characters, return None
    multiple_decimals = re.match(r"\.+.*\.+", num_str)
    if type(num_str) != str or len(num_str) == 0 or multiple_decimals:
        return None



    # Dict to convert the string values to their numeric values
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
            return_val = return_val + (char_to_digit[hex] * 16 ** exponent)
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
            return_val = return_val + (char_to_digit[num]) * 10 ** exponent
            exponent += 1
        if positive:
            return return_val
        else:
            return return_val * -1
    return None



def my_datetime(num_sec):
    pass


def conv_endian(num, endian='big'):
    # validate
    if endian != 'big' and endian != 'little':
        return None
    is_negative = num < 0
    num = abs(num)
    
    # calculate remainders
    remainders = []
    while num > 0:
        remainders.append(num%16)
        num //= 16
    if len(remainders) % 2 == 1:
        remainders.append(0)

    # build byte_strings
    byte_strings = []
    while remainders:
        byte_strings.append("".join( [digit_to_char[remainders.pop()], digit_to_char[remainders.pop()]] ) )
    if endian == 'little':
        byte_strings.reverse()

    # build result
    result = " ".join(byte_strings)
    if is_negative:
        result = "-" + result
    return result