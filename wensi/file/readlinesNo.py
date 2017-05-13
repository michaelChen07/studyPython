#encoding=utf-8

#打印文件指定的行数

def read_file_specific_row(fileName,rowNo):
    try:
        fp=open(fileName,'r')
        row=1
        for line in fp:
            if row==rowNo:
                fp.close()
                return line
            else:
                row+=1
    except Exception,e:
        return "file does not exist! or out of range!"

print read_file_specific_row(r"d:\test\fp2.txt",10)