# encoding=utf-8
import datetime

def get_size(number):
    count = 0
    while(number >= 10):
        number /= 10
        count += 1
    return count + 1

def get_flower(max_int):
    for number in range(max_int):
        if(if_flower(number)):
            print number


def if_flower(number):
    sum = 0
    temp_number = number
    count = get_size(temp_number)
    for j in range(count):
        mod = temp_number % 10
        temp_number /= 10
        sum += pow(mod, count)
        return sum == number

max_int = input("输入最大数: ")
print type(max_int)
start = datetime.datetime.now()
get_flower(max_int)
end = datetime.datetime.now()
print "总共花费时间：" + str((end-start).seconds) + "s"