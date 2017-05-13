#encoding=utf-8
"""“Pig Latin”是一个英语儿童文字改写游戏，整个游戏遵从下述规则：
(1). 元音字母是‘a’、‘e’、‘i’、‘o’、‘u’。字母‘y’在不是第一个字母的情况下，也被视作元音 字母。其他字母均为辅音字母。
例如，单词“yearly”有三个元音字母（分别为‘e’、‘a’和最后一个 ‘y’）和三个辅音字母（第一个‘y’、‘r’和‘l’）。
(2). 如果英文单词以元音字母开始，则在单词末尾加入“hay”后得到“Pig Latin”对应单词。
例如，“ask” 变为“askhay”，“use”变为“usehay”。（同上）
(3). 如果英文单词以‘q’字母开始，并且后面有个字母‘u’，将“qu”移动到单词末尾加入“ay”后得到 “Pig Latin”对应单词。
例如，“quiet”变为“ietquay”，“quay”变为“ayquay”。
(4). 如果英文单词以辅音字母开始，所有连续的辅音字母一起移动到单词末尾加入“ay”后得到“Pig Latin” 对应单词。
例如，“tomato”变为“omatotay”， “school” 变为“oolschay”，“you” 变为 “ouyay”，“my” 变为“ymay ”，“ssssh” 变为“sssshay”。
(5). 如果英文单词中有大写字母，必须所有字母均转换为小写。
输入格式: 一系列单词，单词之间使用空格分隔。
输出格式： 按照以上规则转化每个单词，单词之间使用空格分隔。
输入样例： Welcome to the Python world Are you ready
输出样例： elcomeway otay ethay ythonpay orldway arehay ouyay eadyray
"""
import string

#定义了一个函数，将列表左移指定位。如leftMove([1,2,3,4],2),则返回[3,4,1,2]
def leftMove(list, step):
    Move = list[:step]
    for m in range(step, len(list)):
        list[m-step] = list[m]
    list[len(list)-step:] = Move
    return list

#定义函数，实现字母游戏
def get_chrgame(s):

    #将输入的句子分割，放入列表
    list_chr=list(s.split(" "))

    for i in xrange(len(list_chr)):

        #将每个单词的大写字母改成小写
        if not list_chr[i].islower():
            list_chr[i]=string.lower(list_chr[i])

        #实现条件2，以元音字母开始，则在单词末尾加入“hay”
        if list_chr[i][0] in "aeiou":
            list_chr[i]=list_chr[i]+"hay"

        #实现条件4，以辅音字母开始，所有连续的辅音字母一起移动到单词末尾加入“ay”
        if list_chr[i][0] not in "aeiou":
            new_list=list(list_chr[i])

            #对y开始，y后是元音字母的情况进行处理，先将y移到最后
            new_list=leftMove(new_list,1)

            #调用左移函数，移动结束后+"ay",遇到包含y在内的元音字母，break跳出循环
            for j in xrange(len(new_list)):
                if new_list[j] in "aeiouy":
                    list_chr[i]="".join(leftMove(new_list,j)+["ay"])
                    break

        #实现条件3，以‘q’开始，将“qu”移动到单词末尾加入“ay”
        elif list_chr[i][0:2]=="qu":
            list_chr[i]=list_chr[i][2:]+"quay"


    #返回值，按照要求的格式输出
    return " ".join(list_chr)

s="Welcome to the Python world Are you ready"
print get_chrgame(s)
