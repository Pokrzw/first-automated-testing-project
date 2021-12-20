import re


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
        return 'Wrong input (only upper case letters)'
    return True

def DecodeCaesar(code):
    if CheckRegex(code) is not True:
        return CheckRegex(code)
    else:
        result = ""
        for letter in code:
            result += SearchLetterCode(letter)
        return result
    
    