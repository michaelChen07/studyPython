#encoding=utf-8
def dec_to_bin():
    num = int(raw_input("please input a num:"))
    binlist = []
    while 1:
        quient = num / 2
        binlist.append(str(num%2))
        num = quient
        if num == 0:
            break
    return "".join(binlist[-1::-1])

print dec_to_bin()


