import re
from cezar import *
from doctest import testmod

def ModifyCode(letter_val, a = 1, b = 1):
    '''
    >>> ModifyCode(21, 3, 12)
    23
    '''
    code = ( a * int(letter_val) + b ) % 26
    return code 

def SearchLetterCode(letter, a = 1, b = 1):
    keys, vals = list(CAESAR_DICT.keys()), list(CAESAR_DICT.values())
    letter_index = keys.index(letter)
    new_val = ModifyCode(letter_index,a, b)
    return keys[new_val]

def SearchLetterDecode(letter, a = 1, b = 1):
    if type(a)!=int or type(b)!=int:
        raise TypeError
    else:
        keys, vals = list(CAESAR_DICT.keys()), list(CAESAR_DICT.values())
        letter_index = keys.index(letter)
        result = ""
        aOdwrucon = mnozenie(a)
        pID = aOdwrucon * (letter_index - b) % 26
        if pID < 0:
            pID += 26
        result += keys[pID] 
        return result

def mnozenie(a):
    '''
    >>> mnozenie(23)
    17
    '''
    result = 1
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            result = i
    return result


def CodeAfiniczny(word, a=1, b=1):
    if CheckRegex(word) is not True:
        return CheckRegex(word)
    if type(a)!=int or type(b)!=int:
        raise TypeError
    else:
        result = ""
        for letter in word:
            result += SearchLetterCode(letter, a, b)
        return result

def DecodeAfiniczny(word, a=1, b=1):
    if CheckRegex(word) is not True:
        return CheckRegex(word)
    if type(a)!=int or type(b)!=int:
        raise TypeError
    else:
        result = ""
        for letter in word:
            result += SearchLetterDecode(letter, a, b)
        return result

if __name__ == '__main__':
    testmod(name ='Afiniczny', verbose = True)
