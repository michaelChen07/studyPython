#encoding=utf-8

#从界面输入一些单词，然后写入一个文件，保存后，从文件中找出长 度最长的单词，然后写入到文件的最后。

file_content=raw_input("input your words:")

with open(r"D:\test\fp5.txt","w") as fp:
    fp.write(file_content)

fp=open(r"D:\test\fp5.txt","r+")

#替换句子中的，.
word_list=fp.read().replace(","," ").replace(".","  ").split()

max_length_word=""

for i in range(len(word_list)):
    if len(word_list[i])>=len(max_length_word):
        max_length_word=word_list[i]
print "max_length_word:",max_length_word

#游标放置到文件结尾
fp.seek(0,2)

fp.write(max_length_word)
fp.close()





