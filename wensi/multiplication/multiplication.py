#encoding=utf-8
def mul_nine():
    for a in range(1,10):
        for num in range(1,a+1):
            b = a * num
            print "%d * %d = %d\t"%(num,a,b),#\是转义的意思，'\n'是换行，'\t'是tab
        print"\n"

mul_nine()