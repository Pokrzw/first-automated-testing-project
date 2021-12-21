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

class TestCaesarCode(unittest.TestCase):
    def test_wrong_input(self):
        self.assertEqual(CodeCaesar('LOREm'), 'Wrong input (only upper case letters)')
    def test_correct_input(self):
        self.assertEqual(CodeCaesar('VENI'), 'YHQL')

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

class TestSearchLetterDecode(unittest.TestCase):
    def test_CheckLetterDecode_bad_input_SPECIAL_CHAR(self):
        self.assertEqual(SearchLetterDecode('/'),'Cannot translate this symbol')
    def test_CheckLetterDecode_Y(self):
        self.assertEqual(SearchLetterDecode('Y'),'V')
    def test_CheckLetterDecode_A(self):
        self.assertEqual(SearchLetterDecode('A'),'Z')    
    def test_CheckLetterDecode_B(self):
        self.assertEqual(SearchLetterDecode('B'),'Y')    
    def test_CheckLetterDecode_C(self):
        self.assertEqual(SearchLetterDecode('C'),'X')

class TestDecodeCaesar(unittest.TestCase):
    def test_wrong_input(self):
        self.assertEqual(DecodeCaesar('LOREm'), 'Wrong input (only upper case letters)')
    def test_correct_input(self):
        self.assertEqual(DecodeCaesar('YHQL'), 'VENI')

class TestCaesar(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(Caesar('YHQL', 'decode'), 'VENI')
    def test_code(self):
        self.assertEqual(Caesar('VENI', 'code'), 'YHQL')
    def test_code_no_args(self):
        self.assertEqual(Caesar('VENI'), 'YHQL')
    def test_wrong_action(self):
        self.assertEqual(Caesar('YHQL', 'clean my room'), 'Wrong action')    

if __name__ == "__main__":
    unittest.main()