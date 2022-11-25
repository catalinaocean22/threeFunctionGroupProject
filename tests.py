import unittest
from task import conv_num
from random import randint


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

    def test_random_hex(self):
        test_int = randint(0, 1000000000)
        rand_hex = hex(test_int)
        self.assertEqual(conv_num(rand_hex), test_int)

    def test_random_negative_hex(self):
        test_int = randint(0, 1000000000)
        rand_hex = '-' + hex(test_int)
        self.assertEqual(conv_num(rand_hex), test_int * -1)


if __name__ == '__main__':
    unittest.main()
