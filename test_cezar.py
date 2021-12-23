import unittest
import re
from cezar import *
from exceptions import *
from hamcrest import *
from custom_matcher import eq_to_VENI
from assertpy import *
import pytest
import nose2
from nose2.tools import params


class TestCodeRegex(unittest.TestCase):
    def test_wrong_string_LOWERCASE(self):
        with self.assertRaises(TypeError):
            CheckRegex('lorem')
    def test_wrong_string_NUMBER(self):
        with self.assertRaises(TypeError):
            CheckRegex('123')
    def test_right_string_UPPERCASE(self):
        assert_that(CheckRegex('LOREM')).is_true()

class TestCaesarCode(unittest.TestCase):
    def test_wrong_input(self):
        with self.assertRaises(TypeError):
            CodeCaesar('LOREm')
    def test_correct_input(self):
        assert_that(CodeCaesar('VENI')).is_equal_to('YHQL')

class TestSearchLetterCode(unittest.TestCase):
    @params(
        ('/','Cannot translate this symbol'),
        ('a','Cannot translate this symbol'),
        ('V','Y'),
        ('X','A') ,
        ('Y','B'),
        ('Z','C')
    )
    def test_CheckLetterCode(self,a,b):
        assert SearchLetterCode(a) == b
        
class TestSearchLetterDecode(unittest.TestCase):
    def test_CheckLetterDecode_bad_input_SPECIAL_CHAR(self):
        self.assertEqual(SearchLetterDecode('/'),'Cannot translate this symbol')
    def test_CheckLetterDecode_Y(self):
        self.assertEqual(SearchLetterDecode('Y'),'V')
    def test_CheckLetterDecode_A(self):
        assert_that(SearchLetterDecode('A')).contains_only('Z')    
    def test_CheckLetterDecode_B(self):
        assert_that(SearchLetterDecode('B')).is_equal_to_ignoring_case('Y')    
    def test_CheckLetterDecode_C(self):
        assert_that(SearchLetterDecode('C')).is_alpha()

class TestDecodeCaesar(unittest.TestCase):
    def test_wrong_input(self):
        with self.assertRaises(TypeError):
            DecodeCaesar('LOREm')
    def test_correct_input_YHQL(self):
        assert_that(DecodeCaesar('YHQL'), is_(eq_to_VENI()))

class TestCaesar(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(Caesar('YHQL', 'decode'), 'VENI')
    def test_code(self):
        self.assertEqual(Caesar('VENI', 'code'), 'YHQL')
    def test_code_no_args(self):
        self.assertEqual(Caesar('VENI'), 'YHQL')
    def test_wrong_action(self):
        with self.assertRaises(CezarWrongOption):
            Caesar('YHQL', 'clean my room')    

if __name__ == "__main__":
    unittest.main()
    import nose2
    nose2.main()