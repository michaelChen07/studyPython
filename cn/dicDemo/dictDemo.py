#encoding=utf-8

#根据value查找对应的key
#method 1
dicta={"a":1,"b":2,"c":2}
for key,value in dicta.items():
    if value==2:
        print key

#method 2
def findkey_byValue(d,value):
    keys=[]
    for key in d.keys():
        #print d[key]
        if d[key]==value:
            keys.append(key)
    return keys
dicta={"age":60,"name":"fosterwu","nickname":"fosterwu","sex":"man"}
print findkey_byValue(dicta,"fosterwu")

#如果字典中有这个key则打印对于的value
if dicta.has_key("age"):
    print dicta["age"]

print dicta.get("age",True)#字典中存在age这个值，打印age对应的value
print dicta.get("f",False)#字典中不存在f这个值，则返回设定的默认值False

print dicta.setdefault(2,"3")#字典中不存在这个值，在字典中添加键值对
print dicta.setdefault("age","3")#字典中存在这个值，打印age对应的value,不修改值

dicta.clear()#清空字典
