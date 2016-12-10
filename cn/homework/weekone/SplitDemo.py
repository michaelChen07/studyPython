#encoding=utf-8
"""def splitDemo(s,split_s=" "):
    return s.split(split_s)
print splitDemo("aabbccbbdd","bb")
print splitDemo("aa bbccbbdd")"""

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





