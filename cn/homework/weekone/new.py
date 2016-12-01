#encoding=utf-8
lista = [4,3,6,12,56]
for i in xrange(1,len(lista)):
    lista[i] += lista[i-1]
print lista