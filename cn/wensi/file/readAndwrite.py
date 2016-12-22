#encoding=utf-8

#同时读写文件
fp = open(r"d:\test\fp1.txt","a+")
#print fp.read()

print "*"*30

fp.seek(0,0)
fp.write("I Love You"+"\n")
fp.seek(0,0)
#print fp.read()
fp.close()

#创建一个空文件
fp = open(r"d:\test\fp6.txt","w")
fp.close()

#练习题3：读取文件的前两行
fp = open(r"d:\test\fp1.txt","r")
print fp.readline()
print fp.readline()
fp.close()

print "*"*30

#练习题4：读取文件的奇数行
fp = open(r"d:\test\fp1.txt","r")
row = 1
for line in fp:
    if row%2 == 1:
        row += 1
        print line
    else:
        row += 1


