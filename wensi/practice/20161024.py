#encoding=utf-8
num=int(raw_input("please input a num:"))
if num > 0:
    print "%s > 0"%(num)
elif num == 0:
    print "%s = 0"%(num)
elif num < 0:
    print "%s < 0"%(num)
else:
    print "error"

list_a =[]
for i in range(5):
    num=int(raw_input("please input a num:"))
    list_a.append(num)
print "your input is:",list_a
print "the sum of the num is :",sum(list_a)



#输入a,b,c,d 4个整数，计算a+b-c*d的结果
def date_input():
    lista = []

    for i in "abcd":
        print "please input a num: %s = " %i
        try:
            j = int(raw_input())
            lista.append(int(j))
        except Exception,e:
            print "error,not a number,please try again!"
            return [0]
    return lista

lista = []
while True:
    if len(lista) == 4:
        a, b, c, d = lista[0], lista[1], lista[2], lista[3]
        print "result:a+b-c*d = ",a+b-c*d
        print "success!"
        break
    else:
        lista = date_input()



#3个人在餐厅吃饭，分摊饭费。总费用35.27美元，小费15%。求：每人付多少钱？
#encoding=utf-8
cost_fee = float(raw_input("please input the cost :"))
tip = float(raw_input("please input the tip percent:")) / 100
totalfee = cost_fee * tip + cost_fee
num_people = int(raw_input("please input the number of people:"))
print "totalfee: % .2f" % totalfee
print "fee: % .2f" % (totalfee / 3)


#计算12.5*16.7的矩形的周长和面积，单位：米
length = float(raw_input("please input the length:"))
width = float(raw_input("please input the width:"))
circumference = float((length + width)*2)
forests = float(length * width / 2)
print "circumference: %.1f" % circumference,"m"
print "forests: %.1f" %forests,"m*m"


#7*7*7*7有几种写法
#1
print 7*7*7*7
#2
print pow(7,4)
#3
k = 1
for i in range(4):
    k *= 7
print k
#3
a,k = 1,1
while a < 5 :
    k *= 7
    a += 1
print k



#8 华氏温度转为摄氏温度，C=5/9*（F-32）
ft = raw_input("please input the Fahrenheit:")
try:
    ct = 5 * (float(ft) - 32) / 9
    print "the Celsius temperature is %.2f ℃" % ct
except Exception,e:
    print "the Fahrenheit is error!"



#9 100 ≥ x ≥ 50，折扣10%；x > 100,折扣20%。输入商品价格，显示折扣和实际付款
fee = float(raw_input("please input the price:"))
if fee >= 50 and fee <= 100:
    print "the discount is 10%"
    totalfee = fee * 0.9
if fee > 100:
    print "the discount is 20%"
    totalfee = fee * 0.8
print "the totalfee is %.2f:" % totalfee,totalfee


#10 判断一个数能否同时被3和5整除
num = int(raw_input("please input a num:"))
if num % 3 == 0 and num % 5 == 0:
    print "the num is the times of 3 and 5"
else:
    print "the num is not the times of 3 and 5"


#11 1+2+3+。。。+100
print sum(range(1,101))


#13 age>=10 and age<=12,girl(f),age,循环10次，加入的总人数
sum_people = 0
for i in range(3):
    age = int(raw_input("please input your age:"))
    sex = raw_input("please input your sex (f or m):")

    if age >=10 and age <= 12 and sex == "f":
        print "welcome to join our football team!"
        sum_people += 1
    else:
        print "sorry,we can not play together!"
print "our football team has %d members!" %sum_people


#14 加油站距离20km，缓冲油5L
#1)邮箱容积
#2)剩余油量
#3)车的耗油量
volume = float(raw_input("please input your car's volume(L):"))
remainingfuel = float(raw_input("please input your remainingfuel(L):"))
oilconsumption = float(raw_input("please input your car's oil consumption(L/KM):"))
if (remainingfuel - 5)/oilconsumption < 20:
    addgas = volume - remainingfuel
    print "your need add %.2f gasoline at least" %addgas
else:
    print "your need not add gasoline at this station"
    station = int(((remainingfuel-5)/oilconsumption) / 20)
    print "your can add gasoline at %d next station" %station


#15 面包、热狗、番茄酱、芥末酱、洋葱；面包必订。求订购组合多少种，1订，0不订
lista = [1,0,0,0,0]
a = 0
for i in range(2):
    lista[1] = i
    for j in range(2):
        lista[2] = j
        for k in range(2):
            lista[3] = k
            for l in range(2):
                lista[4] = l
                a += 1
                print lista
print "you can have %d choice" %a


lista = [1,0,0,0,0]
a = 0
b,c,d,e,f = 12,7,5,8,20
print "cal for bread,hotdog,tomato, mustard,onion is :",b,c,d,e,f
for i in range(2):
    lista[1] = i
    for j in range(2):
        lista[2] = j
        for k in range(2):
            lista[3] = k
            for l in range(2):
                lista[4] = l
                a += 1
                cal = 12+7*i+5*j+8*k+l*20
                print lista,",","total cal is :",cal
print "you can have %d choice" %a