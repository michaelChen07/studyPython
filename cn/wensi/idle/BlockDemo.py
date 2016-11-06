# -*- coding: cp936 -*-
# 程序设计三大结构
# 1. 顺序结构
# 2. 分支结构
# 3. 循环结构

# 分支结构
def test_block(grade):
    if 85<=grade<=100:
        print"wonderful"
    elif grade>=75 and grade<85:
        print"good"
    elif grade>=60 and grade<75:
        print"soso"
    else:
        print"fail"

test_block(90)
print("**********************************\n")

# 循环结构
# 
def test_sum():
    add_sum = 0
    for i in range(1,101):
        add_sum=add_sum+i
    return add_sum
    
print test_sum()

