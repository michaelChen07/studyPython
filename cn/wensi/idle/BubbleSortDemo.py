# -*- coding: cp936 -*-

# @author: chenzhen

# 冒泡排序
# 1. 校验： 输入是不是一个列表、元祖， 如果是元祖 --> 列表
# 2. 冒泡排序： 依次比较， 大的放到后面（交换）

def bubble_sort(pend_list):
    if type(pend_list).__name__!="list" and type(pend_list).__name__!="tuple":
        print "please input a list or tuple"
        return # 如果类型不符合， 直接跳出整个函数
    if len(pend_list)<=1:
        print pend_list
        return pend_list#如果序列只有一个值，返回该序列，无需排序
    if type(pend_list).__name__=="tuple":
        list(pend_list)#讲输入的元组转换成列表
    for i in range(1,len(pend_list)):
        for j in range(0,len(pend_list)-i):
            if pend_list[j]>pend_list[j+1]:
                pend_list[j],pend_list[j+1]=pend_list[j+1],pend_list[j]
    return pend_list

def bubble_sort2(pend_list):
    if not isinstance(pend_list, list) and not isinstance(pend_list, tuple):
        print "please input a list or tuple"
        return # 如果类型不符合， 直接跳出整个函数
    if len(pend_list)<=1:
        print pend_list
        return pend_list
    if type(pend_list).__name__=="tuple":
        list(pend_list)
    for i in range(1,len(pend_list)):
        for j in range(0,len(pend_list)-i):
            if pend_list[j]>pend_list[j+1]:
                pend_list[j],pend_list[j+1]=pend_list[j+1],pend_list[j]
    return pend_list

                   
real_list = [31, 4, 5, 1, 3, 5]
print(bubble_sort(real_list))
print("************************************")
real_list1 = [3]
print(bubble_sort(real_list1))
print("************************************")
bubble_sort(34)
print("************************************")

real_list = [31, 4, 5, 1, 3, 5]
print(bubble_sort2(real_list))
print("************************************")
real_list1 = [3]
print(bubble_sort2(real_list1))
print("************************************")
bubble_sort(34)
