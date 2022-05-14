import unittest
import test_code


class test_module_true(unittest.TestCase):

    def test_palindrome_true(self):
        result = test_code.palindrome("acca")
        self.assertTrue(result, False)


if __name__ == '__main__':
    unittest.main()
