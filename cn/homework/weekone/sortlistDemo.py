#encoding=utf-8
#按照列表中元组的长得，进行逆向排序
lista = [(1,2),(3,4,-2),(6,7,8,9)]
def a(tup):
    return len(tup)
lista.sort(key=a,reverse=True)
print lista

#按照最后一个数*5的大小进行逆向排序
listb = [(1,2),(3,4,-2),(6,7,8,9)]
def b(num):
    return (num[-1])*5
listb.sort(key=b,reverse=True)
print listb

#按照所有元组之和进行逆向排序
listc = [(1, 2), (3, 4, -2), (6, 7, 8, 9)]
def c(tup):
    return sum(tup)
listc.sort(key=c,reverse=True)
print listc

