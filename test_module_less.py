import unittest
import test_code


class test_module_less(unittest.TestCase):

    def test_remainder_equal(self):
        result = test_code.find_remainder(10, 2)
        self.assertLess(result, 1)


if __name__ == '__main__':
    unittest.main()
