#encoding=utf-8
#遍历字符串，列表展示
s="gloryroad"

#method 1:
lisa=[]
for i in s:
    lisa.append(i)
print lisa

#method 2:
lisb=[]
for i in xrange(len(s)):
    lisb.append(s[i])
print lisb

#method 3:
print list(s)

#method 4:
print [i for i in s]

#讲小写字母转成大写字母
print s.swapcase()

print "*"*30


#将字符串偶数位置的字符，进行大小写互换
s="gloryroad"
s=list(s)
for i in range(0,len(s),2):
    if ord(s[i])>97 and ord(s[i])<122:
        s[i]=chr(ord(s[i])-32)
    elif ord(s[i])>65 and ord(s[i])<90:
        s[i]=chr(ord(s[i])+32)

print "".join(s)