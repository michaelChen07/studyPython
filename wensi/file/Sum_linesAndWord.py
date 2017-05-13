#encoding=utf-8

#打印文件内容
with open(r"D:\workspace\PycharmProjects\studyPython\readme.txt") as fp:
    content=fp.read()
print content

#文件分割，返回列表
print content.splitlines()

#行数
print len(content.splitlines())

#列表元素拼接
print "".join(content.splitlines())

#字符个数
print len("".join(content.splitlines()))