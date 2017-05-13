#encoding=utf-8
"""import homework.new2
import homework.week5.importstringDemo as p

print p.isdigit("123")
print homework.new2.S_isdigit("abc")"""
import string
word_list=[]

#读取文件内容
with open(r"d:\test\fp1.txt")  as fp:
    content=fp.read()

#替换掉内容中的标点符号
for i in string.punctuation:
    content = content.replace(i,"")

#获取单词列表
for i in content.split():
    word_list.append(i)

#去重，统计出现单词数
for i in set(word_list):
    print i

print "count unique word number:",len(set(word_list))


