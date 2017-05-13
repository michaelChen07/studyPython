#encoding=utf-8
#s=1!+2!+3!+…..+n!
def factorial(n):
    sum = 0
    for i in range(1,n+1):
        result = reduce(lambda x, y: x * y, range(1, i + 1))
        sum += result
    return sum
print factorial(3)


