#coding:utf-8

def findMaxNum(x,y,z):
    if x >=y and x >= z:
        return x
    elif y > z:
        return y
    else:
        return z

if __name__=="__main__":
    numList = raw_input(u"请输入3个数字，以逗号分隔：").split(",")
    print numList
    maxNum = findMaxNum(int(numList[0]),int(numList[1]),int(numList[2]))
    print maxNum
