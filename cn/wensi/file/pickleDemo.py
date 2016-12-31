#encoding=utf-8

#序列化:把变量从内存中变成可存储或传输的过程称之为序列化

import cPickle as cp
a={1:2,2:3}
b=[5,6,7,8]
f=open(r"d:\test\list.data","w")
cp.dump(a,f)
cp.dump(b,f)
f.close()

f=open(r"d:\test\list.data","r")
c=cp.load(f)
d=cp.load(f)
f.close()

print c
print d
