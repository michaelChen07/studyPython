# -*- coding: cp936 -*-
# @author: chenzhen

# ��������
# 1. ��һ�� key ֵ L[0]
# 2. left[], right[], middle[] �Ƚ�
# 3. �ݹ飬left[], right[] �ٽ��п���
# 4. ����ֵ�� left + middle + right

# �ݹ飺
# 1. ��ʼ����
# 2. �����߼��� �����Լ�
# 3. ��������

def quick_sort(L):
    if len(L)<=1:
        return L#ֻ��һ�����֣���������
    key = L[0]
    left = []
    right = []
    middle = []
    for i in range(0,len(L)):
        if L[i]>key:
            right.append(L[i])#��keyֵ�󣬷��ұ�
        elif L[i]<key:
            left.append(L[i])#��keyֵС�������
        elif L[i]==key:
            middle.append(L[i])
#    quick_sort(left)
#    quick_sort(right)
    return quick_sort(left)+middle+quick_sort(right)
                   
real_list = [5, 9, 7, 31, 3, 5]
print(quick_sort(real_list))
