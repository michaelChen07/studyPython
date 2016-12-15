#encoding=utf-8
#已知一字符串列表list1 = ['a','b','c','d', 'e', 'f', 'g']，
# 对序列的任一子序列list1[start, end] 中的元素进行排列组合，有多少种不同的组合，请分别输出

list1 = ['a','b','c','d', 'e', 'f', 'g']
count = 0
for i in range(len(list1)+1):
    for j in range(1,len(list1)+1):
        if j+i<len(list1)+1:
            count += 1
            print "组合：%s"%count,list1[i:j+i]