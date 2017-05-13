#encoding=utf-8
#求一个正整数的阶乘
#方法一：
def factorial(n):
    if n == 0 or n == 1:
        return 1
    number = 1
    for i in range(2,n+1):
        number *= i
    return number
print factorial(4)

#方法二：递归
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
print factorial(4)

#方法三：reduce()函数
n=input('input your number: ')
print reduce(lambda x,y:x*y,range(1,n+1))