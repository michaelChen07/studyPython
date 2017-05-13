#encoding=utf-8
lista = [1,2,3,(1,2,4),"f",(2,5)]
tuplelist = []
for i in range(len(lista)):
    if isinstance(lista[i],tuple):
        tuplelist.extend(lista[i])

for j in tuplelist:
    print j
