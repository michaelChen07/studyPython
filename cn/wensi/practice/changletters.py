#encoding=utf-8
#方法一：用ASCII
def change_charletter(letters):
    "字符串中大写变小写，小写变大写。其余不变"
    list_result = []

    for i in letters:
        if ord(i) > 96 and ord(i) < 123:
            i = chr(ord(i)-32)
            list_result.append(i)
        elif ord(i) > 64 and ord(i) < 91:
            i = chr(ord(i)+32)
            list_result.append(i)
        else:
            list_result.append(i)
    return "".join(list_result)

print change_charletter("Aa1")
print change_charletter.__doc__

#方法二：用string模块
import string
def get_string_capwords(s):
    str=""
    for letter in s:
        if letter in string.lowercase:
            str+=chr(ord(letter)-32)
        elif letter in string.uppercase:
            str+=chr(ord(letter)+32)
        else:
            str+=letter
    return str
print get_string_capwords("A1b2C3d4")