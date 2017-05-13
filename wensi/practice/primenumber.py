#encoding=utf-8
def get_primenumber():
    for i in xrange(1,101):
        ifprime  = 1
        for j in xrange(2,i):
            if i%j == 0:
                ifprime = 0
        if ifprime == 1:
            print i,
get_primenumber()
