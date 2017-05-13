#encoding=utf-8

s="abcdefghijklmnop"

j=0
start=0
for i in range(1,7):
    if start+j<=len(s):
        print s[start:start+j+1]
        start=start+j+1
        j=j+1
    else:
        tmp1=s[start:len(s)]  #把所有字符串剩余的都存到tmp1里面 了
        length=len(s)-start
        start=0
        tmp2=s[start:i-length]#把不够的，从头开始取，存到变量2 里面
        print tmp1+tmp2

