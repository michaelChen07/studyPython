# -*- coding: cp936 -*-
# �����������ṹ
# 1. ˳��ṹ
# 2. ��֧�ṹ
# 3. ѭ���ṹ

# ��֧�ṹ
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

# ѭ���ṹ
# 
def test_sum():
    add_sum = 0
    for i in range(1,101):
        add_sum=add_sum+i
    return add_sum
    
print test_sum()

