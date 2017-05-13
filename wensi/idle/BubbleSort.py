# coding=utf-8

"""冒泡排序"""


def bubble_sort(pend_list):
    if not isinstance(pend_list, list) and not isinstance(pend_list, tuple):  # 元组列表才能排序
        print("输入必须输入列表或者元组")
        return
    if isinstance(pend_list, tuple):  # 元组转成列表
        pend_list = list(pend_list)
    for i in range(1, len(pend_list)):
        for j in range(0, len(pend_list) - i):  # 范围从 0 到 len(list) - 1(找一个例子画一下)
            if pend_list[j] > pend_list[j + 1]:
                pend_list[j], pend_list[j + 1] = pend_list[j + 1], pend_list[j]
    return pend_list


real_list = (3, 34, 1, 45, 12, 3, 6)
print(bubble_sort(real_list))
