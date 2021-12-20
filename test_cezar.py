import unittest
import re
from cezar import *

class TestCodeRegex(unittest.TestCase):
    def test_wrong_string_UPPERCASE(self):
        self.assertEqual(CheckRegex('lorem'),'Wrong input (only upper case letters)')
    def test_wrong_string_NUMBER(self):
        self.assertEqual(CheckRegex('123'),'Wrong input (only upper case letters)')
    def test_right_string_LOWERCASE(self):
        self.assertEqual(CheckRegex('LOREM'), True)

class TestCaesarDecode(unittest.TestCase):
    def test_wrong_input(self):
        self.assertEqual(DecodeCaesar('LOREm'), 'Wrong input (only upper case letters)')
    def test_correct_input(self):
        self.assertEqual(DecodeCaesar('VENI'), 'YHQL')
if __name__ == "__main__":
    unittest.main()