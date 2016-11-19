#encoding=utf-8

#输入某年某月某日，判断这一天是这一年的第几天？
year = int(raw_input("please input the year:"))
month = int(raw_input("please input the month:"))
date = int(raw_input("please input the date:"))
list_date = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day = 0
for i in range(month):
    day += list_date[i]
sumday = day + date
#判断是不是闰年
if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
    print "今年是个闰年"
    loop = 1
if loop == 1 and month > 2:
    sumday = sumday + 1
print "今天是第 %d 天" %sumday
