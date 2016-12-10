#encoding=utf-8

#定义函数，实现内置函数split的功能

#split函数
print "aabbccbbdd".split("bb")
print "aa bbccbbdd".split()

#算法：
#计算切割字符长度，遍历str中的每一个字符，
# 判断每个字符+切割字符长度-1的后续字符是否等于切割字符，若等于把把之前的字符串添加到一个列表中
def splitDemo(s,split_s=" "):
    tmp=""  #存储切割后的字符串
    length=len(split_s) #计算一下切割符的长度
    result=[]
    i=0
    while i<=len(s)-1:  #遍历s中每个字符
        if s[i:i+length]==split_s:  #切割条件
            result.append(tmp)  #切割，把之前的字符串存入result
            tmp=""  #清空，用于下个循环
            i+=length   #跳过length个长度，实现跳过分割符，继续便利
        else:
            tmp+=s[i]   #不是切割点，需要存到tmp中
            i+=1    #加一后跳到下一个字符继续遍历
    result.append(tmp)  #把最后的tmp添加到result中
    return result

print splitDemo("aabbccbbdd","bb")
print splitDemo("aa bbccbbdd")


#method 2:
def split_string(s,split_s):
    result2=[]
    while split_s in s:
        index_split=s.index(split_s)    #切割符首位所在的索引位置
        result2.append(s[:index_split]) #添加字符串首位到切割符首位的字符串
        s=s[index_split+len(split_s):]  #重新定义字符串：未参与切割的部分
    result2.append(s)   #添加最后一次切割剩下的字符串
    return s
print split_string("aabbccbbdd","bb")
print split_string("aa bbccbbdd")

