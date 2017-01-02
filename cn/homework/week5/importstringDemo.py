#encoding=utf-8

import string
def isdigit(s):
    for letter in s:
        if letter not in string.digits:
            return False
        else:
            pass
    return True

def isalphanum(s):
    for letter in s:
        if letter not in string.digits and letter not in string.letters:
            return False
        else:
            pass
    return True
