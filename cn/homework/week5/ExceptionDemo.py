#encoding=utf-8

def print_exception():
    raise ValueError#主动抛出一个异常
try:
    try:
        print_exception()
    except ZeroDivisionError,e:
        print "ZeroDivisionError",e
except ValueError,e:
    print "2：ValueError",e



def valueError():
    int('a')

try:
    try:
        try:
            print 1/0
        except IOError,e:
            print "IOError"
        else:
            print 'done'
    except ZeroDivisionError,e:
        print "ZeroDivisionError"
    valueError()
except ValueError,e:
    print "ValueError"