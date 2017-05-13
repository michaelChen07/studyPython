#encoding=utf-8

#打印1-100行，a-z循环

fp=open("D:\\test\\fp2.txt","w")
letter=97
for i in xrange(1,101):
    if letter<=122:
        fp.write(str(i)+" "+chr(letter)+"\n")
        letter += 1
    else:
        letter=97
        fp.write(str(i) + " " + chr(letter) + "\n")
        letter += 1
fp.close()
