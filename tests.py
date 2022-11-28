import unittest
import random
from task import conv_num, my_datetime, conv_endian
from datetime import datetime


def build_almost_equal_tests(expected, test_case, func_under_test, message):
    def test(self):
        result = func_under_test(test_case)
        self.assertAlmostEqual(expected, result, 5, message.format(test_case, expected, result))
    return test


def build_equal_tests(expected, test_case, func_under_test, message):
    def test(self):
        result = func_under_test(test_case)
        self.assertEqual(expected, result, message.format(test_case, expected, result))
    return test


def build_none_tests(test_case, func_under_test, message):
    def test(self):
        result = func_under_test(test_case)
        self.assertIsNone(result, message.format(test_case, None, result))
    return test


class TestConvNum(unittest.TestCase):

    def hardcoded_tests(self):

        # A hardcoded list of tests from assignment description, edge-cases, and Ed questions
        test_dict = {
            '12345': 12345,
            '-123.45': -123.45,
            '.45': 0.45,
            '123.': 123.0,
            '0xAD4': 2772,
            '0xAZ4': None,
            '12345A': None,
            '12.3.45': None,
            '-': None,
            '.': None,
            '0': 0,
            '0.': 0.0,
            '.0': 0.0,
            '0.0': 0.0,
            '-0': 0,
            '1': 1,
            '-1': -1,
            '1.0': 1.0,
            '-1.0': -1.0,
            '0x': None,
            '0x0000000': 0,
            '0001234': 1234,
            '000.1234': 0.1234,
            '+1234': None,
            '-0000123.45': -123.45,
            '0001': 1,
            '0001000': 1000,
            '0.0001': 0.0001,
            '0.0001000': 0.0001
        }
        message = 'Test case: {}, Expected: {}, Result: {}'
        for key in test_dict.keys():
            if test_dict[key] is None:
                new_test = build_none_tests(key, conv_num, message)
            elif isinstance(test_dict[key], int):
                new_test = build_equal_tests(test_dict[key], key, conv_num, message)
            else:
                new_test = build_almost_equal_tests(test_dict[key], key, conv_num, message)
            setattr(unittest.TestCase, 'test{}'.format(key), new_test)

    def random_int_float_testing(self, tests_to_generate=10000):
        for i in range(tests_to_generate):
            # Generate random integers and floats
            test_num = round(random.uniform(-1000000000, 1000000000), random.randint(0, 50))
            odds = random.randint(0, 1)
            if odds == 1:
                test_num = round(test_num)

            # Generate tests
            message = 'Test case: {}, Expected: {}, Result: {}'
            new_test = build_almost_equal_tests(test_num, str(test_num), conv_num, message)
            setattr(unittest.TestCase, 'test_{}'.format(test_num), new_test)

    def random_hex_testing(self, tests_to_generate=10000):
        # Generate random hexes
        for i in range(tests_to_generate):
            test_int = random.randint(0, 1000000000)
            test_hex = hex(test_int)
            odds = random.randint(0, 1)
            if odds == 1:
                test_hex = '-' + test_hex
                test_int *= -1

            # Generate tests
            message = 'Test case: {}, Expected: {}, Result: {}'
            new_test = build_equal_tests(test_int, test_hex, conv_num, message)
            setattr(unittest.TestCase, 'test_{}'.format(test_hex), new_test)


def unix_to_datetime(seconds):
            return datetime.utcfromtimestamp(seconds)


def string_date_formatter(a_date):
            d = a_date.strftime("%m-%d-%Y")
            return d


class TestMyDateTime(unittest.TestCase):
    # provided example tests
    def test_example_0(self):
        self.assertEqual(my_datetime(0), '01-01-1970')

    def test_example_1(self):
        self.assertEqual(my_datetime(123456789), '11-29-1973')

    def test_example_2(self):
        self.assertEqual(my_datetime(9876543210), '12-22-2282')

    def test_example_3(self):
        self.assertEqual(my_datetime(201653971200), '02-29-8360')

    # random tests from 0 up to the big example
    def test_random(self, tests_to_generate=10000):
        for i in range(tests_to_generate):
            sec = random.randint(0, 253402261199)
            message = 'Test case: {}, Expected: {}, Result: {}'
            new_test = build_equal_tests(string_date_formatter(unix_to_datetime(sec))), sec,  my_datetime, message)
            setattr(unittest.TestCase, 'test_{}'.format(sec), new_test)


class TestConvEndian(unittest.TestCase):
    # provided example tests
    def test_example_0(self):
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_example_1(self):
        self.assertEqual(conv_endian(954786), '0E 91 A2')

    def test_example_2(self):
        self.assertEqual(conv_endian(-954786), '-0E 91 A2')

    def test_example_3(self):
        self.assertEqual(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_example_4(self):
        self.assertEqual(conv_endian(-954786, 'little'), '-A2 91 0E')

    def test_example_5(self):
        self.assertEqual(conv_endian(num=-954786, endian='little'),
                         '-A2 91 0E')

    def test_example_6(self):
        self.assertIsNone(conv_endian(num=-954786, endian='small'))


if __name__ == '__main__':
    TestConvNum.hardcoded_tests(TestConvNum())
    TestConvNum.random_int_float_testing(TestConvNum())
    TestConvNum.random_hex_testing(TestConvNum())
    TestMyDateTime.test_random(TestMyDateTime())
    unittest.main()
