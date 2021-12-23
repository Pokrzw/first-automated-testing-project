import unittest
from afiniczny import *

class TestModifyCode(unittest.TestCase):
    def test_ModifyCode_correct_V(self):
        self.assertEqual(ModifyCode(21, 3, 12), 23)
    def test_ModifyCode_correct_E(self):
        self.assertEqual(ModifyCode(4, 3, 12), 24)

class TestSearchLetterCode(unittest.TestCase):
    def test_CheckLetterCode_correct_input_V_X(self):
        self.assertEqual(SearchLetterCode('V', 3, 12),'X')
    def test_CheckLetterCode_correct_input_E_Y(self):
        self.assertEqual(SearchLetterCode('E', 3, 12),'Y')
    def test_CheckLetterCode_correct_input_N_Z(self):
        self.assertEqual(SearchLetterCode('N', 3, 12),'Z')
    def test_CheckLetterCode_correct_input_I_K(self):
        self.assertEqual(SearchLetterCode('I', 3, 12),'K')

class TestCodeAfiniczny(unittest.TestCase):
    def test_CodeAfiniczny_incorrect_input_NaN(self):
        with self.assertRaises(TypeError):
            CodeAfiniczny('LOREM', 'a',1)
    def test_CodeAfiniczny_incorrect_input_word(self):
        self.assertEqual(CodeAfiniczny('Lorem'), 'Wrong input (only upper case letters)')
    def test_CodeAfiniczny_correct_input(self):
        self.assertEqual(CodeAfiniczny('VENI', 3 ,12), "XYZK")

class TestMnozenie(unittest.TestCase):
    def test_Mnozenie(self):
        self.assertEqual(mnozenie(23),17)

class TestSearchLetterDecode(unittest.TestCase):
    def test_SearchLetterDecode_incorrect(self):
        with self.assertRaises(TypeError):
            SearchLetterDecode('X','A',12)
    def test_SearchLetterDecode_correct(self):
        self.assertEqual(SearchLetterDecode('X',3,12), 'V')

class TestDecodeAfiniczny(unittest.TestCase):
    def test_SearchLetterDecode_correct(self):
        self.assertEqual(DecodeAfiniczny('XYZK',3,12), 'VENI')
    def test_SearchLetterDecode_incorrect_NaN(self):
        with self.assertRaises(TypeError):
            DecodeAfiniczny('XYZK','a',12)
    def test_SearchLetterDecode_incorrect_NaN(self):
        self.assertEqual(DecodeAfiniczny('xyzk'), 'Wrong input (only upper case letters)')


if __name__ == "__main__":
    unittest.main()