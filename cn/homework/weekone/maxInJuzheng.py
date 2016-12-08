#encoding=utf-8
#有一个3*4的矩阵，求出其中值最大的元素，以及其所在行数和列号

#打印一个矩阵
def get_list(h,w):
    for i in xrange(1,h+1):
        for j in xrange(1,w+1):
            print "%2d\t" %(i*j),
        print

#打印3*4的矩阵
get_list(3,4)

#求矩阵中最大值

#以列表代替矩阵
jz_list=[[23,2,3,4],[5,23,7,8],[9,10,11,22]]

#定义一个函数，在一行中找出最大值的索引，因从0开始，所以+1显示位置
def max_index(a):
    return a.index(max(a))+1
#print max_index([1,2,4])#测试此行数功能是否正确


h=0#行
dicta={}
for i in xrange(len(jz_list)):
    h += 1
    print h,max(jz_list[i]),max_index(jz_list[i])#行数，每行最大值，每行最大值的列号
    dicta[(h,max_index(jz_list[i]))]=max(jz_list[i])#定义一个字典，key=每行最大值的行数，列号，value=每行最大值
    print dicta
    b=max(dicta, key=dicta.get)#字典values最大，对应的key值
print "最大值=%s"%(dicta.get(b))#显示最大值的行数和列号
print "最大值的（行数，列号）",b
#此方法的缺点，如果有多个最大值，只会显示一个最大值的位置