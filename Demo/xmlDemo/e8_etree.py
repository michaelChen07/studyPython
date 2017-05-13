# encoding=utf-8

import sys
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

tree = ET.ElementTree(file=r'C:\Users\Administrator\Documents\HBuilderProject\GetStart\xml\e8_movies_etree.xml')
# 获取根目录
root = tree.getroot()
print root.tag
print root.attrib

#打印根目录的下一级子目录
for child_of_root in root:
    print child_of_root.tag
    print "********", child_of_root.attrib

print "*" * 50
print root[0].tag
print root[0].text
print root[0][0].tag
print root[0][0].text
print "*" * 50


for elem in tree.iter():  # 遍历根元素，所有子元素；所有的movie标签和movie下的子标签
    print elem.tag, elem.attrib

# 统计movie的个数
print len([elem.tag for elem in tree.iter() if elem.tag == "movie"])


print "*" * 50
for elem in tree.iterfind('movie/type'):  # 查找movie下的所有type标签
    print elem.tag, elem.attrib

for i in tree.findall("movie"):
    print "movie:", i, i.tag, i[0].tag, i[0].text

for i in tree.findall("movie/format"):
    print "movie:", i, i.tag, i.tag, i.text

print "*" * 50
for elem in tree.iter('tag=stars'):  # 查找标签为star的元素
    print elem.tag, elem.attrib
print "*" * 50
for elem in tree.iterfind('*[@title="Ishtar"]'):  # 查找属性为title="Ishtar"的元素
    print elem.tag, elem.attrib

print "-" * 50
root = tree.getroot()  # 获取<collection>元素
print "root:", root[0].tag  # 打印第一级movie元素的标签，为movie
print "subnode:", root[0][0].tag  # 打印第一级movie元素下的第一个子元素标签type
print "subnode:", root[0][1].tag  # 打印第一级movie元素下的第二个子元素标签format
print "subnode:", root[0][2].tag  # 打印第一级movie元素下的第三个子元素标签year
print "subnode:", root[0][3].tag  # 打印第一级movie元素下的第四个子元素标签rating

print "subnode:", root[0][4].tag  # 打印第一级movie元素下的第五个子元素标签stars
del root[0][4]  # 删除第一级movie元素下的第四个子元素
del root[0][3]  # 删除第一级movie元素下的第三个子元素
del root[0][2]  # 删除第一级movie元素下的第二个子元素
del root[0][1]  # 删除第一级movie元素下的第一个子元素

del root[3]  # 删除第四个movie元素
del root[2]  # 删除第三个movie元素
for subelem in root:
    print subelem.tag, subelem.attrib  # 打印第一个movie和第二个movie元素的标签和属性

tree.write(sys.stdout)  # 将xml文件的内容写到屏幕上
# tree.write("d:\\movies.xml")  #将变更的xml文件写入到文件中