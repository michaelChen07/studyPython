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
                print "回答正确"
                break
            if oops == maxtries:
                print "正确答案是\n %s%d"%(pr,ans)
            else:
                print "回答错误 ... 再试一次"
                oops += 1
        except(KeyboardInterrupt,EOFError,ValueError):
            print "输入错误 ... 再试一次"

def main():
    while True:
        doprob()
        try:
            opt = raw_input("继续? [y/n]").lower()
            if opt and opt[0] =="n":
                break
        except(KeyboardInterrupt,EOFError):
            break

if __name__ == "__main__":
    main()


