#coding=utf-8
import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tree = ET.parse(r'C:\Users\Administrator\Documents\HBuilderProject\GetStart\xml\e8_movies_etree.xml')

count = 0
for elem in tree.iter(tag='movie'): #遍历树中的movie节点
    print elem.tag
    if elem[0].text == 'War, Thriller':
        count += 1
print count

#以下代码实现了边读文件边解析的作用，节省了内存
count = 0
for event, elem in ET.iterparse(r'C:\Users\Administrator\Documents\HBuilderProject\GetStart\xml\e8_movies_etree.xml'):  #遍历所有xml文件中的标签
    #print elem.tag
    if event == 'end':  #检测“闭合的”(end)事件，标签关闭
        if elem.tag == 'type' and elem.text == 'War, Thriller':  #标签为type，且文本内容为War, Thriller ,则count+1
            count += 1
            print "find!"
    elem.clear() #清除元素内容，包含元素内容和属性等。

print count

#事件
#start 在元素打开时触发。数据和元素的子元素仍不可用。
# end 在元素关闭时触发。所有元素的子节点，包括文本节点，现在都是可用的。
#close 在解析完成后触发。
