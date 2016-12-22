#encoding=utf-8

#实现字符串的upper、lower以及swapcase方法

import string
#实现upper方法
def get_upper(s):
    letter=""
    for i in xrange(len(s)):
        if s[i] in string.uppercase:
            letter += chr(ord(s[i])+32)
        else:
            letter += s[i]
    return letter

print get_upper("ABCabc12")

#实现lower方法
def get_lower(s):
    letter=""
    for i in xrange(len(s)):
        if s[i] in string.lowercase:
            letter += chr(ord(s[i])-32)
        else:
            letter += s[i]
    return letter

print get_lower("ABCabc12")

#实现swapcase方法
def get_swapcase(s):
    letter=""
    for i in xrange(len(s)):
        if s[i] in string.lowercase:
            letter += chr(ord(s[i])-32)
        elif s[i] in string.uppercase:
            letter += chr(ord(s[i])+32)
        else:
            letter += s[i]
    return letter

print get_swapcase("ABCabc12")