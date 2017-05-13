# encoding=utf-8

#  输入数字a，n，如a，4，则打印a+aa+aaa+aaaa之和

#方法一：
def get_sum(a, n):
    sum = 0
    for i in range(n):
        sum += a * pow(10, i) * n
        n -= 1
    return sum

print get_sum(3, 3)

#方法二：
def aiy(a,n):
    sum = 0
    for i in range(1,n+1):
        sum += int(str(a)*i)
    print sum

aiy(3,3)