import unittest
import re
from morse import *

class Test_CheckLetterDecode(unittest.TestCase):
    def test_read_A(self):
        self.assertEqual(CheckLetterDecode('.-'), 'A')
    def test_read_T(self):
        self.assertEqual(CheckLetterDecode('-'), 'T')
    def test_read_H(self):
        self.assertEqual(CheckLetterDecode('....'), 'H')        
    def test_incorrect_input_NONEXISTENT_LETTER(self):
        self.assertEqual(CheckLetterDecode('.-.--.-.'), 'No such letter in Morse code')
    def test_incorrect_input_EMPTY_STRING(self): 
        self.assertEqual(CheckLetterDecode(''), 'No such letter in Morse code')
    def test_incorrect_input_MANY_SPACES(self):    
        self.assertEqual(CheckLetterDecode('    '), 'No such letter in Morse code')
    def test_ONE_SPACE(self):
        self.assertEqual(CheckLetterDecode(' '), '')

class Test_CheckLetterCode(unittest.TestCase):
    def test_read_A(self):
        self.assertEqual(CheckLetterCode('A'), '.-')
    def test_read_T(self):
        self.assertEqual(CheckLetterCode('T'), '-')
    def test_read_H(self):
        self.assertEqual(CheckLetterCode('H'), '....')    
    def test_SPACE(self):
        self.assertEqual(CheckLetterCode(" "),'     ')
    def test_ERR_ASTERISK(self):
        self.assertEqual(CheckLetterCode('*'), 'Cannot translate this symbol')

class Test_CheckRegexDecode(unittest.TestCase):
    def test_correct_input_no_spaces(self):
        self.assertEqual(CheckRegexDecode('.-.'), True)
    def test_correct_input_with_spaces(self):
        self.assertEqual(CheckRegexDecode('. ---. -'), True)
    def test_incorrect_imput_letter(self):
        self.assertEqual(CheckRegexDecode("A"), False)
    def test_incorrect_imput_number(self):
        self.assertEqual(CheckRegexDecode(6), False)

class Test_CheckRegexCode(unittest.TestCase):
    def test_correct_input_letter(self):
        self.assertEqual(CheckRegexCode('ABC'), True)
    def test_correct_input_letter_WITHSPACE(self):
        self.assertEqual(CheckRegexCode('ABC DEF'), True)
    def test_correct_input_number(self):
        self.assertEqual(CheckRegexCode(123), True)
    def test_correct_input_number_and_letter(self):
        self.assertEqual(CheckRegexCode('ABC 123'), True)
    def test_incorrect_imput_dot(self):
        self.assertEqual(CheckRegexCode("."), False)
    def test_incorrect_imput_dash(self):
        self.assertEqual(CheckRegexCode('-'), False)

class TestMorseDecode(unittest.TestCase):
    def test_MorseDecode_incorrect_input(self):
        self.assertEqual(MorseDecode("ABC"), "Wrong Expression")
    def test_MorseDecode_incorrect_spaces(self):
        self.assertEqual(MorseDecode('.- .-..   .-'), 'Incorrect word')
    def test_MorseDecode_incorrect_letter(self):
        self.assertEqual(MorseDecode('--.--'), 'No such letter in Morse code')
    def test_MorseDecode_incorrect_letter_in_correct_sentence(self):
        self.assertEqual(MorseDecode('---.--- - .-.. .-     -- .-     -.- --- - .-'),'No such letter in Morse code')    
    def test_MorseDecode_correct_AA(self):
        self.assertEqual(MorseDecode('.- .-'), "AA")
    def test_MorseDecode_correct_ALA_MA_KOTA(self):
        self.assertEqual(MorseDecode('.- .-.. .-     -- .-     -.- --- - .-'), "ALA MA KOTA")

class TestMorse(unittest.TestCase):
    def test_CheckLetterDecode(self):
        pass    
        


if __name__ == "__main__":
    unittest.main()