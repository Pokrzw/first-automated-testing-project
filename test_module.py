import unittest
import re
from morse import *
from cezar import *
from exceptions import *
from hamcrest import *
from assertpy import * 
import pytest
import nose2
from nose2.tools import params
from custom_matcher import eq_to_VENI
from afiniczny import *

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


class TestSearchLetterCodeCaesar(unittest.TestCase):
    def test_CheckSearchLetterCaesarSlash(self):
        assert SearchLetterCodeCaesar('/') == 'Cannot translate this symbol'
    def test_CheckSearchLetterCaesarLowerCase(self):
        assert SearchLetterCodeCaesar('a') == 'Cannot translate this symbol'
    def test_CheckSearchLetterCaesarXtoA(self):
        assert SearchLetterCodeCaesar('X') == 'A'

            
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

class TestModifyCode(unittest.TestCase):
    def test_ModifyCode_correct_V(self):
       assert_that(ModifyCode(21, 3, 12)).is_positive()
    def test_ModifyCode_correct_E(self):
        self.assertEqual(ModifyCode(4, 3, 12), 24)

class TestSearchLetterCode(unittest.TestCase):
    def test_CheckLetterCode_correct_input_V_X(self):
        assert_that(SearchLetterCode('V', 3, 12)).is_equal_to('X')
    def test_CheckLetterCode_correct_input_E_Y(self):
        self.assertEqual(SearchLetterCode('E', 3, 12),'Y')
    def test_CheckLetterCode_correct_input_N_Z(self):
        assert_that(SearchLetterCode('N', 3, 12)).contains('Z')
    def test_CheckLetterCode_correct_input_I_K(self):
        self.assertEqual(SearchLetterCode('I', 3, 12),'K')

class TestCodeAfiniczny(unittest.TestCase):
    def test_CodeAfiniczny_incorrect_input_NaN(self):
        assert_that(calling(CodeAfiniczny).with_args('LOREM', 'a',1), raises(TypeError))            
    def test_CodeAfiniczny_incorrect_input_word(self):
        assert_that(calling(CodeAfiniczny).with_args('Lorem'), raises(TypeError))
    def test_CodeAfiniczny_correct_input(self):
        self.assertEqual(CodeAfiniczny('VENI', 3 ,12), "XYZK")

class TestMnozenie(unittest.TestCase):
    def test_Mnozenie(self):
        assert_that(mnozenie(23), greater_than_or_equal_to(17))

class TestSearchLetterDecode(unittest.TestCase):
    def test_SearchLetterDecode_incorrect(self):
        assert_that(calling(SearchLetterDecode).with_args('X','A',12), raises(TypeError))            
    def test_SearchLetterDecode_correct(self):
        assert_that(SearchLetterDecode('X',3,12), starts_with('V'))            

class TestDecodeAfiniczny(unittest.TestCase):
    def test_SearchLetterDecode_correct(self):
        assert_that(DecodeAfiniczny('XYZK',3,12), contains_string('VENI'))
    def test_SearchLetterDecode_incorrect_NaN(self):
        assert_that(calling(DecodeAfiniczny).with_args('XYZK','a',12), raises(TypeError))            
    def test_SearchLetterDecode_incorrect_NaN(self):
        assert_that(calling(DecodeAfiniczny).with_args('xyzk'), raises(TypeError))


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
def test_CheckLetterMorseCodeParam(letter, result):
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
        self.assertEqual(CheckRegexCode('ABC! 123?'), True)
    def test_incorrect_imput_dot(self):
        self.assertEqual(CheckRegexCode("."), True)
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
    def test_MorseDecode_correct_special(self):
        assert_that(MorseDecode('.- -... -.-. -.-.--     .---- --..-- ..--- ...--')).is_equal_to('ABC! 1,23')

class TestMorseCode(unittest.TestCase):
    def test_MorseCode_incorrect_imput(self):
        self.assertEqual(MorseCode('.-'),"Cannot translate this word")
    def test_MorseCode_correct_letter_A(self):
        self.assertEqual(MorseCode('A'), '.-')
    def test_MorseCode_correct_letters_AB(self):
        self.assertEqual(MorseCode('AB'), '.- -...')
    def test_MorseCode_correct_letters_with_space_AB_CD(self):
        self.assertEqual(MorseCode('AB CD'), '.- -...     -.-. -..')
    def test_MorseCode_correct_interpunction(self):
        assert_that(MorseCode('ABC! 1,23')).is_equal_to('.- -... -.-. -.-.--     .---- --..-- ..--- ...--')

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
    unittest.main()
    # nose2.main()