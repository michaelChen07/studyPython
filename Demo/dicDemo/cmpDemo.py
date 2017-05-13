#encoding=utf-8

#字典比较：先比较键值对数，再比较key，最后比较value

dicta={"a":1,"b":1,"c":1}
dictb={"a":1,"b":1}
dictc={"d":1,"b":1,"c":1}
dictd={"a":1,"b":1,"c":1}
print cmp(dicta,dictb)
print cmp(dicta,dictc)
print cmp(dicta,dictd)

print str(dicta)
print len(dicta)