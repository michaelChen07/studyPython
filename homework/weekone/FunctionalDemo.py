#encoding=utf-8
#max()
array1 = range(6)
array2 = range(0, 20, 3)
print "array1: ", array1
print "array2: ",  array2
print('max(array1)=', max(array1))
print('max(array2)=', max(array2))
print('max(array1,)=', max(array1, key=lambda x: x > 3) )#此处根据X>3返回是Ture\False,max返回第一个Ture对应的值

print(max('ah', 'bz', key=lambda x: x[1]))#此处根据lambda返回是h/z，z>h,max返回"bz"
print(max(array1, array2, key=lambda x: x[1]))#此处根据x[1]返回是1/3，3>1,max返回array1

def comparator(x):
   return x[2]
print(max('ah2', 'bf3', key=comparator))#此处根据x[2]返回是3/2，3>2,max返回bf3