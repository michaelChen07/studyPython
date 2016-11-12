#encoding=utf-8
t = [1,24,[3,4,5],('a','b','c'), 8, 9]
for i in range(len(t)):
    if isinstance(t[i],(list,tuple)):
        for j in t[i]:
            print j,#将列表和元组中的元素打印到一行
        print#换行
    else:
        print t[i]