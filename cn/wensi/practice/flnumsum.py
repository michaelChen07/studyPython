#encoding=utf-8
def sum(num):

    fp_write = open(r"C:\Users\Administrator\Desktop\good.txt","w")
    for i in range(1,num+1):
        fp_write.write(str(i)+"\n")
    fp_write.close()

    fp_read = open(r"C:\Users\Administrator\Desktop\good.txt","r")
    fpnum = 0
    for eachline in fp_read:
        fpnum = fpnum + int(eachline)
    return fpnum
print sum(100)


