# coding=utf-8

"""快速排序"""


# 校验函数，对输入的列表或者元组进行校验
def list_check(pend_list):
    if not isinstance(pend_list, list) and not isinstance(pend_list, tuple):  # 元组列表才能排序
        print("输入必须输入列表或者元组")
        return
    if isinstance(pend_list, tuple):  # 元组转成列表
        pend_list = list(pend_list)
        return pend_list


# 三个列表递归实现快排： 优点是比较好理解，小的放到左边，大的放到右边，一样的放到中间， 然后将三个列表加起来变成一个
# 时间复杂度：最理想 O(nlogn) 最差时间O(n^2)
def quick_sort(pend_list):

    if len(pend_list) < 1: return pend_list # 终止条件，没有这个条件就会一直跑下去直到数组越界

    key = pend_list[0]
    left_list = []
    middle_list = []
    right_list = []

    for i in range(0, len(pend_list)):
        if key > pend_list[i]:
            left_list.append(pend_list[i])
        elif key < pend_list[i]:
            right_list.append(pend_list[i])
        else:
            middle_list.append(pend_list[i])

    return quick_sort(left_list) + middle_list + quick_sort(right_list)

#  三行代码搞定快速排序
def quick_sort2(L):
    if len(L) <= 1: return L
    return quick_sort2([lt for lt in L[1:] if lt < L[0]]) + [L[0]] + quick_sort2([ge for ge in L[1:] if ge >= L[0]])


# 标准快排
# 递归：
# 1. 原问题可以被划分为类似子问题
# 2. 结束条件： i >= j
def quick_sort3(L, low, high):

    i = low  # 游标 i
    j = high  # 游标 j
    if i >= j:
        return L

    key = L[low] # 比较的参考值
    while i < j:
        while i < j and L[j] >= key: # j 不断向前，小的放到前面
            j -= 1
        L[i] = L[j]
        while i < j and L[i] < key: # i 不断向后， 大的放到后面
            i += 1
        L[j] = L[i]
    L[i] = key
    quick_sort3(L, low, i-1)
    quick_sort3(L, j+1, high)
    return L


real_list = [3, 34, 1, 45, 12, 3, 6]
print("******************* 三个列表递归实现快排 *********************")
print(quick_sort(real_list))

print("******************* 三行代码搞定快速排序 *********************")
print(quick_sort2(real_list))

print("******************* 标准快速 *********************")
print(quick_sort3(real_list, 0, len(real_list)-1))