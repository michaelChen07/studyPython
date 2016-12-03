#encoding=utf-8

#找出列表中第二大的数
a=[1,2,3,4,4,5,5,5,6,6,6]

#method1
max_value=max(a)
while 1:
    if max_value in a:
        a.remove(max_value)
    else:
        break
print "1:",max(a)

#method2
a=[1,2,3,4,4,5,5,5,6,6,6]
a.sort()

for i in a[::-1]:
    if i!=max(a):
        print "2:",i
        break

#method3
a.sort()
b=list(set(a))
print "3:",b[-2]


#method4
print "4:",sorted(list(set(set(a[:]))),reverse=True)[1]

#method5
print "5:",sorted(set(a))[-2]
