#encoding=utf-8
#用递归法遍历多重列表中的值
lista = [1,2,3,[4,5,(6,7)]]
listb = []
def chrinlist(lista):
    for i in lista:
        if not isinstance(i,(tuple,list)):
            #print i
            listb.append(i)#此处必须用全局变量
        else:
            chrinlist(i)
    return listb
print chrinlist(lista)