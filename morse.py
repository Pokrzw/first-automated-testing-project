import re

def Morse(word):
    word = str(word)
    reg = '(\.|-|\s)+'
    if re.fullmatch(reg, word) is None:
        return 'Wrong Character'
    else:
        return "a"

