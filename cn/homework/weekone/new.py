#encoding=utf-8
import copy
lista=[1,2,3,4,[5,6,7]]
listb=copy.deepcopy(lista)
listc=copy.copy(lista)

#改变lista一维的值
lista[0]=9
print "lista=",lista
print "listb=",listb
print "listc=",listc

#分隔符
print "_"*30

#改变lista二维的值
lista[4][0]=8
print "lista=",lista
print "listb=",listb
print "listc=",listc