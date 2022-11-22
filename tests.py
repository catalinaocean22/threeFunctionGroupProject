import unittest
from task import conv_num, my_datetime, conv_endian


class TestConvNum(unittest.TestCase):

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


if __name__ == '__main__':
    unittest.main()
