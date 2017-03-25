#encoding=utf-8
#统计出词频最高的长度大于等于2的单词及其出现的频率。
import re

def count_words(file_path):
    with open(file_path, "r") as fp:
        content = fp.read()
    word_list = re.findall(r"\b[A-Za-z-]+",content,re.I)

    word_dict = {}
    for word in word_list:
        if len(word) >= 2:
            word_dict[word] = word_list.count(word)

    frequency = sorted(word_dict.iteritems(), key=lambda d: d[1], reverse=True)
    return frequency[0]


file_path = r"frequency.txt"
print count_words(file_path)