#encoding=utf-8

#一个文件有很多英文单词，找到出现次数最多的字母，将字母和出现次数加在第一行，其他文件内容加后面，原文保持不变。

import string

#获取文件内容
with open(r"D:\test\fp6.txt","r") as fp:
    file_content=fp.read()
print file_content

#方法1：通过list转dict
"""list_count=[]
for i in file_content:
    if i.isalpha():
        list_count.append(i)
print list_count

dict_max={}
for j in list_count:
    dict_max[j]=list_count.count(j)
print dict_max"""


#方法2：直接用dict。
dict_max={}
for i in file_content:
    if i.isalpha():
        if dict_max.has_key(i):
            dict_max[i] += 1
        else:
            dict_max[i] = 1
print dict_max


# 获取出现次数最多的字母，和该字母出现的次数
def get_maxchr(t):
    for k, v in t.items():
        if t[k] == max(t.values()):
            return k, v
print get_maxchr(dict_max)

#写入文件
fp = open(r"D:\test\fp7.txt","w")
new_file_content=str(get_maxchr(dict_max))+"\n"+file_content
fp.write(new_file_content)
fp.close()


