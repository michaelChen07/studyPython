#encoding=utf-8
from fractions import Fraction
a = 1
b = 1
sum = 0
for i in xrange(20):
    a,b=a+b,a#先计算=右边的值，再赋值给左边，和分开写的意义不一样,这里a+b=2=a=2,a=1=b=1
    #a=a+b 此时a+b=2,所以a=2
    #b=a    此时赋值，b=a=2
    print a,b,Fraction(a,b)
    sum += Fraction(a,b)
print sum






