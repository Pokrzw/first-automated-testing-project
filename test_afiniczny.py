import unittest
from afiniczny import *
from hamcrest import *
from assertpy import *
import pytest



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


if __name__ == "__main__":
    unittest.main()
    import nose2
    nose2.main()