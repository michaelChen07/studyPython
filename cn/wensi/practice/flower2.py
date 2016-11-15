#encoding=utf-8
import math

def myPow(n):
    return int(math.pow(int(n), 3))

for i in xrange(100, 1000):
    res = sum(map(myPow, list(str(i))))
    if res == i:
        print i



