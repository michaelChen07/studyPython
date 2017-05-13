#encoding=utf-8
import os
dir_path = r"d:\test"
os.chdir(dir_path)#操作前一定记得要先切换当前目录到指定目录下
for i in os.listdir(dir_path):
    try:
        if os.path.isdir(i):
            os.rmdir(i)
    except WindowsError:
        continue

