#encoding=utf-8
#fp.seek(0,0)#第二个0表示文件起始位置，第一个零表示偏移量，(0,0)表示最开始位置，(1,0)，文件的第二个位置
#fp.seek(2,1)：1表示从相对位置来定位，2表示偏移量；(-1,1)表示从当前位置向前移动一个字符
#fp.seek(0,2)：2表示从文件末尾来定位，0表示偏移量，(-1,2)从文件结尾向前移动一个字符

fp = open(r"d:\test\fp7.txt","r+")
fp.seek(0,2)
fp.write('!')
fp.seek(0,0)
fp.write('?')
fp.seek(5,0)
fp.write('&')
fp.close()

#练习1：文件写入1-9，4-6替换成9
fp=open(r"d:\test\fp4.txt","w+")
for i in range(1,10):
    fp.write(str(i))

fp.seek(3,0)#3的位置写入9，起始位置向后移3位
fp.write("9")

fp.seek(0,1)#当前位置写入9
fp.write("9")

fp.seek(-4,2)#结尾向前移4位，写入9
fp.write("9")

fp.close()


def write_position(fp_path,position,word):
    with open(fp_path, "r+") as fp:
        max_position = len(fp.read())
        if position > max_position:
            fp.seek(0, 2)
            fp.write(str(word))
        else:
            fp.seek(position - 1, 0)
            fp.write(str(word))


if __name__ == "__main__":
    write_position("e:\\a.txt", 100, "gloryroad")