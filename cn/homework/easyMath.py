#coding=utf-8
#算术游戏

from operator import add,sub
from random import randint,choice

ops = {"+":add,"-":sub}
maxtries = 3#最多回答次数

def doprob():
    op = choice("+-")
    num = [randint(1,10) for i in range(2)]
    num.sort(reverse=True)#按从大到小的顺序排列
    ans = ops[op](*num)
    pr = "%d %s %d = "%(num[0],op,num[1])
    oops = 1
    while True:
        try:
            if int(raw_input(pr)) == ans:
                print "correct"
                break
            if oops == maxtries:
                print "answer\n %s%d"%(pr,ans)
            else:
                print "incorrect ... try again"
                oops += 1
        except(KeyboardInterrupt,EOFError,ValueError):
            print "invalid input ... try again"

def main():
    while True:
        doprob()
        try:
            opt = raw_input("Again? [y/n]").lower()
            if opt and opt[0] =="n":
                break
        except(KeyboardInterrupt,EOFError):
            break

if __name__ == "__main__":
    main()


