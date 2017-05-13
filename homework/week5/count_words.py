#encoding=utf-8

#统计出词频最高的长度大于等于2的单词及其出现的频率。
import re

def count_words(file_path):
    with open(file_path, "r") as fp:
        content = fp.read()

    #匹配文件中的单词，列表的形式返回
    word_list = re.findall(r"\b[A-Za-z-]+",content,re.I)

    #单词和出现次数，存入字典
    word_dict = {}
    for word in word_list:
        if len(word) >= 2:
            word_dict[word] = word_list.count(word)

    #适用用多个最大值的情况
    max_value = 0
    max_keys = []
    for k, v in word_dict.items():
        if v >= max_value:
            if v > max_value:
                max_value = v
                max_keys = [k]
            else:
                max_keys.append(k)
    return max_keys,max_value


    #对字典按value值进行排序，缺点是有多个最大值，不能全部输出
    #frequency = sorted(word_dict.iteritems(), key=lambda d: d[1], reverse=True)
    #return frequency[0]

file_path = r"frequency.txt"
print count_words(file_path)