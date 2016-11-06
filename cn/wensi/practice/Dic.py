#encoding=utf-8
#字典dic={key：value}
dict_b={}
dict_b["a"]="hello"
dict_b["b"]="world"
dict_b["c"]="!"
print dict_b
for key in dict_b:#打印字典中的key值
    print key
for value in dict_b.values():#打印字典中的value值
    print value
for k,v in dict_b.items():#打印字典中的key和value值
    print str(k)+":"+str(v)

dict_b["c"]="good"#修改字典中c对应的value值
print dict_b

#元组tuple=（）
#元组中的值不能修改和删除
#将列表转化为元组
tuple_a=tuple(range(10))
print tuple_a

for i in range(len(tuple_a)):
    if i % 2 == 0:
        print tuple_a[i]

#当元组只有一个值时，需添加，
tuple_a=(1,)
tuple_b=(2,)
print tuple_a+tuple_b