# -*- coding: utf-8 -*-

# 索引 list[]
list=[1,2,3]
print list[0]

# 切片 a[开始值：结束值：步长】
a="0123456789"
print a[3:5]
print a[6:0:-2]

# if 条件语句
flag=False
if flag:
    print "welcome to python!"
else:
    print"welcome to php!"

#elif  多条件判断
score=input("please input score:")
score=int(score) #转换成整数型
if score > 85:
    print "good"
elif 60<score<=85:
    print "pass"
else:
    print "fail"

#elif  多条件判断+or/and
x=int(input("please input score x:"))
y=int(input("please input score y:"))
if x>60 and y>60:
    print "pass all"
elif x>60 or y>60:
    print "pass one"
else:
    print "fail"

#闰年判断
year=int(input("please input the year:"))
if (year%100==0 and year%400==0) or(year%100 != 0 and year%4==0):
    print "%d is leap year"%year
else:
    print "%d is not leap year" %year

# for 循环
for i in "abcd":
    print i

# for 循环+列表
list=["sunday","monday","tuesday",
      "wednesday","thursday","friday",
      "sarturday"]
for i in list:
    print i
    
# for 循环6次
for i in [1,1,1,1,1,1]:
    print "hello python"

#for 循环+range,对1到100求和
sum=0
for i in range(1,101):#rang(1,101)从1取到100
    sum+=i#sum=sum+i
print sum

#for 循环+索引
list=["sunday","monday","tuesday",
      "wednesday","thursday","friday",
      "sarturday"]
for i in range(len(list)):#len()列表的长度
    print list[i]

#for else
for i in range(10):
    print i
    if i==1:
        pass#代码桩，仅占位，不做任何操作
    if i==2:
        print"22222"
        continue#跳过当前循环，继续下一次循环
    if i==5:
        break#跳出本次循环
    print "*"*20
else:
    print "bye"

#循环嵌套
#用for循环实现冒泡排序
lt=[45,13,24,3]
for i in range(1,len(lt)):#用-i替换-1,所以i从1开始取值
    for j in range(0,len(lt)-i):
        if lt[j]>lt[j+1]:
            lt[j],lt[j+1]=lt[j+1],lt[j]#交换位置
            print lt
    
#冒泡排序完整版
def func(lt=[]):
    if type(lt).__name__!="list" and type(lt).__name__!="tuple":
        return
    if type(lt).__name__=="tuple":
        lt=list(lt)
    if len(lt)<=1:
        return
    else:
        for i in range(1,len(lt)):#用-i替换-1,所以i从1开始取值
            for j in range(0,len(lt)-i):
                if lt[j]>lt[j+1]:
                    tmp=lt[j]
                    lt[j]=lt[j+1]
                    lt[j+1]=tmp
    return lt
lt=[45,13,24,3]
tp=(2,6,1,9,4)
print func(lt)
print func(tp)

#while循环，适用于满足某个条件，就无限循环的情况
i=0
sum=0
while (i<100):
    i+=1
    sum+=i
print sum
#print reduce(lambda x,y:x+y,range(1,101))此行代码也可实现从1加到100的和

#例子i<7 and i%2==0
i=0
while i<10:
    i+=1
    if i%2!=0:
        continue
    elif i>7:
        break
    else:
        print i
        
#连续运算
a=float(input("please input a number:"))
while 1:#符合条件，一直执行循环
    b=raw_input("please input an operator:")#此次用input会报错
    c=float(input("please input a number:"))
    if b=="+":
        print "result:",a+c
        a=a+c
    elif b=="-":
        print "result:",a-c
        a=a-c
    elif b=="*":
        print "result:",a*c
        a=a*c
    elif b=="/":
        print "result:",a/c
        a=a/c
    else:
        print "input error.please input as:+-*/"
        break
    
#字典进行简化，相当于switch
a=float(input("please input a number:"))
while 1:#符合条件，一直执行循环
    b=raw_input("please input an operator:")
    c=float(input("please input a number:"))
    result={
        "+":a+c,
        "-":a-c,
        "*":a*c,
        "/":a/c
        }
    a=result.get(b)
    print a 
    
#函数
def printsrt(str):#形式参数
    "print the input string to the standard display device"
    print str
    return
printstr("welcome to python")#实际参数

#例一
def pet(x,y):
    print "i want a",x,y
pet("black","dog")
#例二
def pet(x="white",y):#x此处是缺省参数，既默认值
    print "i want a",x,y
pet("dog")
#例三
def f(x,y):
    print "my name is %s,i'm %d"%(x,y)
    #f("zz",18)
t=("zz",18)
f(*t)#加*可把元组的值赋给x,y
d={"x":"zz","y":18}
f(**d)#加**可把字典的值赋给x,

#冗余参数
def f(x,*args):#加*的形参-元组，加**的形参-字典
    print x
    print args
f(1,2,3)

#返回值return
def fun(x,y):
    if x>y:
        return 1
    elif x>y:
        return -1
    else:
        return 0
print fun(2,1)

#局部变量和全局变量
a=1#全局变量
def fun():
    a=2#局部变量，仅在函数内有效
    global b#强制定义全局变量,函数调用此定义才生效
    b=3
fun()
print a,b

#匿名函数
func=lambda x,y:x*y
print func(2,4)

#常用计算函数
abs()#取绝对值
max()
min()
len()
divmod()#取两个数的商和模
pow(2,3)#2的三次幂
round(x,y)#x的值保留y位小数
help()#了解某个函数的作用
callable()#判断某个函数是否可调用
isinstance()#判断某个数据的类型
cmp()#比较两个数的大小
range()
xrange()
#类型转化函数
hex()#16进制
oct()#8进制
chr()#返回该10进制数对应的ASCII码
ord()#返回该ASCII码对应的10进制数
#string函数
str.capitalize()#首字母大写
str.replace()#对字符串进行替换
str.split()#对字符串进行分割
#序列处理函数
filter()#按某个条件进行过滤
zip()
map()
reduce()

#快速排序（递归调用）
def func(lt=[]):
    if len(lt)<=1:
        return lt
    key=lt[0]
    lt_l=[]
    lt_r=[]
    lt_m=[]

    for i in lt:
        if i<key:
            lt_l.append(i)#小于基准值，放左边
        elif i>key:
            lt_r.append(i)#大于基准值，放右边
        else:
            lt_m.append(i)
            
    lt_l=func(lt_l)
    lt_r=func(lt_r)
    return lt_l+lt_m+lt_r

lt=[12,34,2,5,8,1,9]
print func(lt)






