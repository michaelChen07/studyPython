#encoding=utf-8

#统计笔记的行数，空行不计入

#删除空行
"""def delblanklines(fp_path):
    fp = open(fp_path)
    alist=[]
    for line in fp:
        if line.strip():
            alist.append(line)
    fp.close()
    with open(fp_path,"w") as fp:
        fp.writelines(alist)"""




def count_code_lines_number(file_path):
    line_number=0
    with open(file_path) as fp:
        for line in fp:
            if "__" in line:
                continue
            elif line.strip()=="":
                continue
            elif line.strip()[0]=="#":
                continue
            else:
                line_number+=1
    return line_number

if __name__=="__main__":
    print count_code_lines_number(ur"D:\test\笔记.txt")
