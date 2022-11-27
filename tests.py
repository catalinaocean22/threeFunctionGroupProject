import unittest
from task import conv_num
from task import my_datetime
from task import conv_endian
from random import randint


class TestConvNum(unittest.TestCase):
    # simple tests?
    # todo - required? useful?
    def test_simple_0(self):
        self.assertEqual(conv_num('0'), 0)

    def test_simple_1(self):
        self.assertEqual(conv_num('1'), 1)

    def test_simple_2(self):
        self.assertEqual(conv_num('-1'), -1)

    # invalid input
    # todo

    # provided example tests
    def test_example_1(self):
        self.assertEqual(conv_num('12345'), 12345)

    def test_example_2(self):
        self.assertEqual(conv_num('-123.45'), -123.45)

    def test_example_3(self):
        self.assertEqual(conv_num('.45'), 0.45)

    def test_example_4(self):
        self.assertEqual(conv_num('123.'), 123.0)

    def test_example_5(self):
        self.assertEqual(conv_num('0xAD4'), 2772)

    def test_example_6(self):
        self.assertIsNone(conv_num('0xAZ4'))

    def test_example_7(self):
        self.assertIsNone(conv_num('12345A'))

    def test_example_8(self):
        self.assertIsNone(conv_num('12.3.45'))

    # zeroes at ends tests - leading and trailing
    def test_zeroes_at_ends_1(self):
        self.assertEqual(conv_num('0001'), 1)

    def test_zeroes_at_ends_2(self):
        self.assertEqual(conv_num('0001000'), 1000)

    def test_zeroes_at_ends_3(self):
        self.assertEqual(conv_num('0.0001'), 0.0001)

    def test_zeroes_at_ends_4(self):
        self.assertEqual(conv_num('0.0001000'), 0.0001)

    # random testing
    def test_random_negative_hex(self):
        test_int = randint(0, 1000000000)
        rand_hex = '-' + hex(test_int)
        self.assertEqual(conv_num(rand_hex), test_int * -1)

    def test_random_hex(self):
        test_int = randint(0, 1000000000)
        rand_hex = hex(test_int)
        self.assertEqual(conv_num(rand_hex), test_int)


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
    
    def test_example_3(self):
        self.assertEqual(my_datetime(68256000), '03-01-1972')
        
    def test_example_3(self):
        self.assertEqual(my_datetime(68256599), '03-01-1972')
        
    def test_example_3(self):
        self.assertEqual(my_datetime(194400000), '02-29-1976')
        
    def test_example_3(self):
        self.assertEqual(my_datetime(194486400), '03-01-1976')
    
    def test_example_3(self):
        self.assertEqual(my_datetime(5555555555), '01-18-2146')


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
    unittest.main()
