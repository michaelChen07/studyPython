#encoding=utf-8

def print_exception():
    raise ValueError
try:
    try:
        print_exception()
    except ZeroDivisionError,e:
        print "ZeroDivisionError",e
except ValueError,e:
    print "ValueError",e



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