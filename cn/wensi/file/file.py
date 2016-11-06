#encoding=utf-8
# 1 输入文件名
# 2 打开输入的文件
# 3 显示该文件的内容
# 4 关闭

# 操作基本完成
# Question：
# 1. 写文件由覆盖模式改成追加模式
# 2. 文件写入内容由用户指定， 增加写文件函数参数 file_content
# 3. 读文件：
#       example: lijinlong 的话写入 lijinlong.txt
#                chenzhen 的话写入 chenzhen.txt
# 4. 文件路径问题： 绝对路径，相对路径
# 5. 命名规范：
#       包名: 小写名词
#       模块名: 小写名词
#       变量名: 小写名词, “_” 分隔
#       函数名: 小写动词（_小写名词）

# 读文件，打印
def read_file(file_name):

    try:
        file = open(file_name, "r")
        for eachline in file:
            print eachline
        file.close()
    except Exception, e:
        print "sorry,the file can't be find"

def read_file_with(file_name):
    try:
        with open(file_name, "r") as file:
            for eachline in file:
                print eachline
    except Exception, e:
        print "sorry,the file can't be find"

def write_file(file_name):

    try:
        file = open(file_name, "w")
        file.write("are you ok")
        file.close()
    except Exception, e:
        print "sorry,the file can't be find"

# 测试
read_file_name = raw_input("please input the path of the read_file:")
read_file(read_file_name)
write_file_name = raw_input("please input the path of the write_file:")
write_file(write_file_name)
read_file_name = raw_input("please input the path of the read_file:")
read_file_with(read_file_name)