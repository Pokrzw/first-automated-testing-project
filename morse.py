import re
from doctest import testmod
from exceptions import *

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', '?':'..--..', '!':'-.-.--', 
                    '.':'.-.-.-', ',':'--..--', ';':'---...'}

def CheckLetterDecode(letter):
    '''
    >>> CheckLetterDecode("--...")
    '7'
    '''
    for key in MORSE_CODE_DICT:
        if letter == MORSE_CODE_DICT[key]:
            return key
    if letter == " ": 
        return ""
    else:
        return 'No such letter in Morse code'

def CheckLetterCode(letter):
    for key in MORSE_CODE_DICT:
        if letter == key:
            return MORSE_CODE_DICT[key]
    if letter == " ": 
        return "   "
    else:
        return 'Cannot translate this symbol'

def CheckRegexDecode(word):
    word = str(word)
    reg = '(\.|-|\s)+'
    if re.fullmatch(reg, word) is None:
          return False
    return True 

def CheckRegexCode(word):
    word = str(word)
    reg = '^[A-Z0-9|.|,|!|?|;|:|\s]*$'
    if re.fullmatch(reg, word) is None:
          return False
    return True 

def MorseDecode(word):
    '''
    >>> MorseDecode("ABC")
    'Wrong Expression'
    
    >>> MorseDecode(".- .-")
    'AA'
    '''
    if CheckRegexDecode(word) is False:
        return "Wrong Expression"
    else:
        final_result, cur_letter = "", ""
        iterator, space_count = 0, 0
        for character in word:
            iterator += 1
            if character!=" " and space_count>1 and space_count!=5:
                return "Incorrect word"
            if space_count == 5:
                    final_result += " "  
                    space_count = 0
            if character == " ":
                space_count += 1
                if CheckLetterDecode(cur_letter) != 'No such letter in Morse code':
                    final_result += CheckLetterDecode(cur_letter)
                    cur_letter = '' 
            else:
                space_count = 0
                cur_letter += character
                if iterator == len(word):
                    if CheckLetterDecode(cur_letter) != 'No such letter in Morse code':
                        final_result += CheckLetterDecode(cur_letter)
                    else:
                        return CheckLetterDecode(cur_letter)
        return final_result


def MorseCode(word):
    if CheckRegexCode(word) is False:
        return "Cannot translate this word"
    else:
        final_result = ""
        for letter in word:
            final_result += CheckLetterCode(letter) 
            final_result += ' '
    return final_result[:-1]

def Morse(word, option="code"):
    '''
    >>> Morse(".-", "decode")
    'A'
    >>> Morse("HELLO WORLD", 'code')
    '.... . .-.. .-.. ---     .-- --- .-. .-.. -..'
    '''
    if option=="decode":
        return MorseDecode(word)
    elif option=="code":
        return MorseCode(word)
    else:
        raise MorseWrongOption

if __name__ == '__main__':
    testmod(name ='Morse', verbose = True)