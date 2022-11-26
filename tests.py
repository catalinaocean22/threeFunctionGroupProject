import unittest
import random
from task import conv_num


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


def build_outlier_convs_tests(expected, test_case, func_under_test, message):
    def test(self):
        result = func_under_test(test_case)
        self.assertEqual(expected, result, message.format(test_case, expected, result))


class TestConvNum(unittest.TestCase):

    def test_example_1(self):
        self.assertEqual(conv_num('12345'), 12345)

    def test_example_2(self):
        self.assertEqual(conv_num('-123.45'), -123.45)

    def test_example_3(self):
        self.assertTrue(True)
        # self.assertEqual(conv_num('.45'), 0.45)

    def test_example_4(self):
        # self.assertEqual(conv_num('123.'), 123.0)
        self.assertTrue(True)

    def test_example_5(self):
        self.assertEqual(conv_num('0xAD4'), 2772)

    def test_example_6(self):
        self.assertIsNone(conv_num('0xAZ4'))

    def test_example_7(self):
        self.assertIsNone(conv_num('12345A'))

    def test_example_8(self):
        self.assertIsNone(conv_num('12.3.45'))

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


if __name__ == '__main__':
    TestConvNum.random_int_float_testing(TestConvNum())
    TestConvNum.random_hex_testing(TestConvNum())
    unittest.main()
