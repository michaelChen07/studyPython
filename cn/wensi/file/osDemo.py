#encoding=utf-8

import os

#获取当前工作目录
print os.getcwd()

#更改当前目录
os.chdir(r"D:\workspace\PycharmProjects\studyPython\cn\wensi\practice")
print os.getcwd()

#当前工作目录下的文件
print os.listdir(os.getcwd())

#指定目录下的文件
print os.listdir(r"D:\test")

#返回当前目录
print os.curdir

#创建指定级数的目录
def create_multiple_dir(dir_path,depth,dir_name):
    try:
        os.chdir(dir_path)
    except Exception,e:
        return -1
    for i in range(depth):
        os.mkdir(dir_name+str(i))
        os.chdir(dir_name+str(i))
        with open(dir_name+str(i)+".txt","w") as fp:
            fp.write(dir_name+str(i))
    return 0

print create_multiple_dir("e:\\test",5,"gloryroad")
