import unittest
import re
from morse import *
from exceptions import *
from hamcrest import *
from assertpy import * 
import pytest
import nose2

#assert_that(theBiscuit, equal_to(myBiscuit))
class Test_CheckLetterDecode(unittest.TestCase):
    def test_read_A(self):
        assert_that(CheckLetterDecode('.-'), equal_to('A'))
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

@pytest.mark.parametrize(
    ('letter', 'result'),
    (
        ('A', '.-'),
        ('T', '-'),
        ('H', '....'),
        (" ",'   '),
        ('*', 'Cannot translate this symbol')
    )
)
def test_CheckLetterCode(letter, result):
    assert CheckLetterCode(letter) == result

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

class TestMorseCode(unittest.TestCase):
    def test_MorseCode_incorrect_imput(self):
        self.assertEqual(MorseCode('.-'),"Cannot translate this word")
    def test_MorseCode_correct_letter_A(self):
        self.assertEqual(MorseCode('A'), '.-')
    def test_MorseCode_correct_letters_AB(self):
        self.assertEqual(MorseCode('AB'), '.- -...')
    def test_MorseCode_correct_letters_with_space_AB_CD(self):
        self.assertEqual(MorseCode('AB CD'), '.- -...     -.-. -..')

class TestMorse(unittest.TestCase):
    def test_morse_wrong_option(self):
        with self.assertRaises(MorseWrongOption):
            Morse('SLOWO','Zla opcja')
    def test_decode_regex(self):
        assert_that(Morse('.-','decode')).matches('^[A-Z0-9|\s]*$')
    def test_decode(self):
        self.assertEqual(Morse('.-','decode'),'A')
    def test_code_regex(self):
        assert_that(Morse("HELLO WORLD", 'code')).matches('(\.|-|\s)+')
    def test_code(self):
        assert_that(Morse("HELLO WORLD", 'code')).is_equal_to('.... . .-.. .-.. ---     .-- --- .-. .-.. -..')
    def test_code_no_option(self):
        self.assertEqual(Morse("ALA MA KOTA"),'.- .-.. .-     -- .-     -.- --- - .-')
if __name__ == "__main__":
    import nose2
    nose2.main()
    unittest.main()