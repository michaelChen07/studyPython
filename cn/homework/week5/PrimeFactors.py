#encoding=utf-8
#将一个正整数分解质因数
import math

result = []

def get_PrimeFactors(num):

    i = 2
    square = int(math.sqrt(num)) + 1

    while i <= square:
        if num % i == 0:
            result.append(i)
            get_PrimeFactors(num / i)
            i += 1
            break
        i += 1
    if i > square:
        result.append(num)
    return result

print get_PrimeFactors(40)


