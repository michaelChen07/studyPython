#encoding=utf-8
#原代码
def get_yanghui():
    b=[1]
    while 1:
        yield b
        b=[1]+[b[i]+b[i+1] for i in range(len(b)-1)]+[1]

def print_yanghui(n):
    a=0
    for t in get_yanghui():
        for i in t:
            print i,
        print "\n"
        a+=1
        if a==n:
            break
print_yanghui(10)



#龙宝宝修改后的
def get_yanghui(num):
    b=[1]
    while 1:
        yield " " * num + str(b)
        b = [1] + [b[i] + b[i + 1] for i in range(len(b) - 1)] + [1]
        num -= 1

def print_yanghui(n):
    a=0
    num = n
    for t in get_yanghui(num):
        print t + "\n",
        a += 1
        if a == n:
            break
print_yanghui(10)
