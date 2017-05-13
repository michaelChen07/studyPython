# encoding = utf-8

list1 = [1,2,3,4,5,6,7,8,9]
for i in range(1,len(list1),2):
    list1[i] = list1[0]

result = list(set(list1))

#print result


s = "abcecefagaca"

for i in range(0,len(s)-3):
    if s[i] == s[i+2]:
        s = s[:i]+s[i+2:]
print s




