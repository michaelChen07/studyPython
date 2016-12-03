#encoding=uft-8

#找出列表中第二大的数

#method1
a=[1,2,3,4,4,5,5,5,6,6,6]

max_value=max(a)
while 1:
    if max_value in a:
        a.remove(max_value)
    else:
        break
print max(a)

#method2
a=[1,2,3,4,4,5,5,5,6,6,6]
a.sort()

for i in a[::-1]:
    if i!=max(a):
        print i
        break

#method3
a=[2,5,8,8,0,5]
b=set(a)
b.remove(max(b))
print max(b)


#method4
a=[2,5,8,8,0,5]
sorted(list(set(copy.deepcopy(a))),reverse=True)[1]