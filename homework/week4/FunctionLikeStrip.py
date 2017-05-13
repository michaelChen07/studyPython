#encoding=utf-8
# 从开头遍历，如果和空白字符相等，则去掉
# 从结尾遍历，如果和空白字符相等，则去掉
# 剩余的保留

def string_strip(source_str, strip_str=None):
    space_letter_list = [" ", "\n", "\r", "\t"]
    letter_list = list(source_str)
    if strip_str is None:
        for index in range(len(letter_list)):
            if letter_list[index] in space_letter_list:
                letter_list[index] = ""
            else:
                break
        for index in range(-1, -len(letter_list), -1):
            if letter_list[index] in space_letter_list:
                letter_list[index] = ""
            else:
                break
    else:
        for index in range(len(letter_list)):
            if letter_list[index] == strip_str:
                letter_list[index] = ""
            else:
                break
        for index in range(-1, -len(letter_list), -1):
            if letter_list[index] == strip_str:
                letter_list[index] = ""
            else:
                break
    return "".join(letter_list)


print "'%s'" % string_strip("\t\r\n  a b  \t\r\n ")
print "'%s'" % string_strip("**a*b**", "*")
