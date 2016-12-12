#encoding=utf-8

#检测密码强度
#c1 : 长度>=8 c2: 包含数字和字母 c3: 其他可见的特殊字符
# 强：满足c1,c2,c3 中: 只满足任一2个条件 弱：只满足任一1个或0个条件

import string

def checkPassword(s):
    c1=c2=c3=0
    if len(s) >= 8:#判断密码长度
        c1=1
    for i in s:
        if i.isalnum():#判断密码是否包含数字和字母
            c2=1
        if i in string.punctuation:#判断密码是否包含其他可见的特殊字符
            c3=1

    if c1+c2+c3==3:
        return "high"
    elif c1+c2+c3==2:
        return "Middle"
    elif c1+c2+c3 < 2:
        return "Lower"

#test
print checkPassword("abc!1234")
print checkPassword("abc")
print checkPassword("abc!")