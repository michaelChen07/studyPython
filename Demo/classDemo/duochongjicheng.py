#coding=utf-8
class A(object):
    def __init__(self):
        print "A constructor"
    def a_method(self):
        print "call a_method"
    def method(self):
        print "A method"

class B(A):
    def __init__(self):
        print "B constructor"
        A.__init__(self)
    def b_method(self):
        print "call b_method"
    def method(self):
        print "B method"

class C(A):
    def __init__(self):
        print "C constructor"
        A.__init__(self)
    def c_method(self):
        print "call c_method"
    def x(self):
        print "C method"

class D(C, B):
    def x(self):
        print "D method"
    def d_method(self):
        print "call d_method"

d = D()
d.method()

