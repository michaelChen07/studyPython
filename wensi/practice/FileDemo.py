#encoding=utf-8
#创建文件

#引入模块
import os
ls = os.linesep

# 创建文件
def create_file():
    file_name = raw_input("Please input the file name to create:")
    while True:
        if os.path.exists(file_name):
            print "error: '%s' already exists" % file_name
        else:
            break

    content = []
    print "please input lines:"
    while True:
        entry = raw_input("> ")
        if entry == ".":
            break
        else:
            content.append(entry)

        with open(file_name, "w") as file:
            file.writelines(["%s%s" % (x, ls) for x in content])

        print "Done!"


create_file()


