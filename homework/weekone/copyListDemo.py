#encoding=utf-8
lista=[1,2,4,5,6]

#引用复制:引用复制的list，它们的内存地址是相 同的，修改任何一个list，另一个list 中的元素的值都会被改变。

listb=lista
print "lista",lista
print "listb",listb

print "id(lista)",id(lista)
print "id(listb)",id(listb)

listb[1]=7
print "lista",lista
print "listb",listb
print "_"*30

#非引用复制:非引用list，它们的内存地址不 一样，所以修改任何一个list都 不会影响另一个list
listc=lista[:]
print "lista",lista
print "listc",listb
print "id(lista)",id(lista)
print "id(listc)",id(listc)
listc[1]=9
print "lista",lista
print "listc",listc