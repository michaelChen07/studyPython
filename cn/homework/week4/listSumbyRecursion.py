#encoding=utf-8

#递归实现列表求和,适合多元列表


lista=[1,2,[3,4,5],(6,7)]

def get_sumlist(lista):
    sum = 0
    for i in lista:
        if isinstance(i,(list,tuple)):
            sum += get_sumlist(i) #多元列表再次调用
        else:
            sum += i
    return sum

print get_sumlist(lista)