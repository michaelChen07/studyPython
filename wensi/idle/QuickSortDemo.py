# -*- coding: cp936 -*-
# @author: chenzhen

# 快速排序：
# 1. 找一个 key 值 L[0]
# 2. left[], right[], middle[] 比较
# 3. 递归，left[], right[] 再进行快排
# 4. 返回值： left + middle + right

# 递归：
# 1. 初始条件
# 2. 处理逻辑： 调用自己
# 3. 结束条件

def quick_sort(L):
    if len(L)<=1:
        return L#只有一个数字，无需排序
    key = L[0]
    left = []
    right = []
    middle = []
    for i in range(0,len(L)):
        if L[i]>key:
            right.append(L[i])#比key值大，放右边
        elif L[i]<key:
            left.append(L[i])#比key值小，放左边
        elif L[i]==key:
            middle.append(L[i])
#    quick_sort(left)
#    quick_sort(right)
    return quick_sort(left)+middle+quick_sort(right)
                   
real_list = [5, 9, 7, 31, 3, 5]
print(quick_sort(real_list))
