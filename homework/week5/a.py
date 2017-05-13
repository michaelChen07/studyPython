#encoding=utf-8
import re

pattern = re.compile(r'(\w+) (\w+)')
candidateStr = 'i say, hello world!'
#\2, \1表示分组引用，分别代表第二个分组，第一个分组
print pattern.sub(r'\2 \1', candidateStr)
print re.sub(r'(\w+) (\w+)',r'\2 \1', candidateStr)

#当repl为方法时，将匹配的结果m传入方法
def func(matcher):
    return matcher.group(1).title() + ' ' + matcher.group(2).title() #title():首字母大写

print re.sub(pattern, func, candidateStr)
resultStr = pattern.sub(func, candidateStr)
print resultStr




