# -*- coding: cp936 -*-

# @author: chenzhen

# ð������
# 1. У�飺 �����ǲ���һ���б�Ԫ�棬 �����Ԫ�� --> �б�
# 2. ð������ ���αȽϣ� ��ķŵ����棨������

def bubble_sort(pend_list):
    if type(pend_list).__name__!="list" and type(pend_list).__name__!="tuple":
        print "please input a list or tuple"
        return # ������Ͳ����ϣ� ֱ��������������
    if len(pend_list)<=1:
        print pend_list
        return pend_list#�������ֻ��һ��ֵ�����ظ����У���������
    if type(pend_list).__name__=="tuple":
        list(pend_list)#�������Ԫ��ת�����б�
    for i in range(1,len(pend_list)):
        for j in range(0,len(pend_list)-i):
            if pend_list[j]>pend_list[j+1]:
                pend_list[j],pend_list[j+1]=pend_list[j+1],pend_list[j]
    return pend_list

def bubble_sort2(pend_list):
    if not isinstance(pend_list, list) and not isinstance(pend_list, tuple):
        print "please input a list or tuple"
        return # ������Ͳ����ϣ� ֱ��������������
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
