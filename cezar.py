import re
from doctest import testmod
from exceptions import *

CAESAR_DICT = {
    "A": "0",
    "B": "1",
    "C": "2",
    "D": "3",
    "E": "4",
    "F": "5",
    "G": "6",
    "H": "7",
    "I": "8",
    "J": "9",
    "K": "10",
    "L": "11",
    "M": "12",
    "N": "13",
    "O": "14",
    "P": "15",
    "Q": "16",
    "R": "17",
    "S": "18",
    "T": "19",
    "U": "20",
    "V": "21",
    "W": "22",
    "X": "23",
    "Y": "24",
    "Z": "25",
}

def SearchLetterCode(letter):
    '''
    >>> SearchLetterCode("VENI")
    'Cannot translate this symbol'
    '''

    '''
    >>> SearchLetterCode("V")
    'Y'
    '''
    keys, vals = list(CAESAR_DICT.keys()), list(CAESAR_DICT.values())
    for key in CAESAR_DICT:
        if key == letter:
            i = int(CAESAR_DICT[key]) + 3
            if i>25:
                i = (i % 25) - 1
            return keys[vals.index(str(i))]
    return 'Cannot translate this symbol'

def CheckRegex(code):
    reg = '^[A-Z]*$'
    if re.fullmatch(reg, code) is None:
        raise TypeError
        #return 'Wrong input (only upper case letters)'
    return True

def CodeCaesar(code):
    if CheckRegex(code) is not True:
        return CheckRegex(code)
    else:
        result = ""
        for letter in code:
            result += SearchLetterCode(letter)
        return result
    
def SearchLetterDecode(letter):
    keys, vals = list(CAESAR_DICT.keys()), list(CAESAR_DICT.values())
    for key in CAESAR_DICT:
        if key == letter:
            i = int(CAESAR_DICT[key]) - 3
            if i < 0:
                i =  25 - int(CAESAR_DICT[key])
                
            return keys[vals.index(str(i))]
    return 'Cannot translate this symbol'
    
def DecodeCaesar(code):
    if CheckRegex(code) is not True:
        return CheckRegex(code)
    else:
        result = ""
        for letter in code:
            result += SearchLetterDecode(letter)
        return result

def Caesar(code, action = "code"):
    '''
    >>> Caesar("VENI")
    'YHQL'
    '''

    '''
    >>> Caesar("YHQL", 'decode')
    'VENI'
    '''
    if action is "code" or action is None:
        return CodeCaesar(code)
    if action is "decode":
        return DecodeCaesar(code)
    raise CezarWrongOption

if __name__ == '__main__':
    testmod(name ='Cezar', verbose = True)
