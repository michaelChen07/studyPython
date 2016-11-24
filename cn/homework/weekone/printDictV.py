#encoding=utf-8
#7.一个字符串 list，每个元素是 1 个 ip，输出出现次数最多的 ip

lista = ["eoef","feo","a","a","a","b","b","b","b"]
dica = {}
count = 1
for s in lista:
    dica[s] = lista.count(s)#字符和出现次数以键值对的形式放入字典
print dica
print max(dica,key = dica.get)#输出字典values最大，对应的key值



