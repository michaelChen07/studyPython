# encoding=utf-8

import xml.dom.minidom
import codecs

#在内存中创建一个空的文档
doc = xml.dom.minidom.Document()
print doc

#创建一个根节点
root = doc.createElement('classDemo')

# 给根节点root添加属性
root.setAttribute('name', u'测试开发培训班')

#将根节点添加到文档对象中
doc.appendChild(root)

# 给根节点添加一个叶子节点
students = doc.createElement(u'学生')
teacher = doc.createElement(u'讲师')

# 叶子节点下再嵌套叶子节点
address = doc.createElement("address")
address.appendChild(doc.createTextNode(u"北京"))

teacheraddress = doc.createElement("address")
teacheraddress.appendChild(doc.createTextNode(u"北京"))

# 给节点添加文本节点
name = doc.createElement('name')
name.appendChild(doc.createTextNode(u'陈真'))

teachername = doc.createElement('name')
teachername.appendChild(doc.createTextNode(u'吴老师'))

# 将各叶子节点添加到父节点中
students.appendChild(name)
students.appendChild(address)

teacher.appendChild(teachername)
teacher.appendChild(teacheraddress)

# 然后将company添加到根节点companys中
root.appendChild(students)
root.appendChild(teacher)
print doc.toxml()

#生成xml文档
fp = codecs.open(r'C:\Users\Administrator\Documents\HBuilderProject\GetStart\xml\e6_classDemo.xml', 'w','utf-8')
doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding="utf-8")
fp.close()