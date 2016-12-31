#encoding=utf-8
import os
for root,dirs,files in os.walk(r"d:\test"):
    for file in files:
        print "绝对路径：",os.path.join(root,file)



file_list=[]
dir_list=[]
for root,dirs,files in os.walk("d:\\test"):
    for file in files:
        file_list.append(os.path.join(root,file))

    for dir in dirs:
        dir_list.append(os.path.join(root,dir))

for file in file_list:
    print file

for dir in dir_list:
    print dir


for root, dirs, files in os.walk("e:\\test",topdown=False) :
    print u"上级目录:",root #打印目录绝对路径
    for name in files :
        print u'文件名：',os.path.join(root,name) #打印文件绝对路径

    for name in dirs :
        print u'目录名：',name #打印目录绝对路径

import os

if os.path.exists("e:\\test\\a.py"):
    with open("e:\\test\\a.py","a") as fp:
        fp.write("gloryroad")
else:
    with open("e:\\test\\a.py","a") as fp:
        pass