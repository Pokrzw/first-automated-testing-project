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

class TestSearchLetterCode(unittest.TestCase):
    def test_CheckLetterCode_bad_input_SPECIAL_CHAR(self):
        self.assertEqual(SearchLetterCode('/'),'Cannot translate this symbol')
    def test_CheckLetterCode_bad_input_LOWERCASE(self):
        self.assertEqual(SearchLetterCode('a'),'Cannot translate this symbol')
    def test_CheckLetterCode_normal_case(self):
        self.assertEqual(SearchLetterCode('V'),'Y')
    def test_CheckLetterCode_A(self):
        self.assertEqual(SearchLetterCode('X'),'A')    
    def test_CheckLetterCode_B(self):
        self.assertEqual(SearchLetterCode('Y'),'B')    
    def test_CheckLetterCode_C(self):
        self.assertEqual(SearchLetterCode('Z'),'C')
if __name__ == "__main__":
    unittest.main()