#encoding=utf-8

#当前时间加输入的单词


import time
with open("d:\\x.txt","w+") as fp:
    for i in range(5):
        word=raw_input("please input a word:")
        write_time=time.strftime("%Y-%m-%d %H:%M:%S")
        fp.write(write_time+":"+word+"\n")
    fp.seek(0,0)
    print fp.read()



#encoding=utf-8
import time
def get_current_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")
with open("d:\\x.txt","w+") as fp:
    for i in range(5):
        word=raw_input("please input a word:")
        fp.write(get_current_time()+":"+word+"\n")
    fp.seek(0,0)
    print fp.read()

#encoding=utf-8
import os
#复制文件
def copy_file(source_file_path,destine_file_path):
    if os.path.exists(source_file_path):
        fp1=open(source_file_path,"rb")
        fp2=open(destine_file_path,"wb")
        for line in fp1:
            fp2.write(line)
        fp1.close()
        fp2.close()

copy_file("d:\\test.rar","d:\\gl.rar")


