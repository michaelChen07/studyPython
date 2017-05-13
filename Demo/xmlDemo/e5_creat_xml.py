# encoding=utf-8

import xml.dom.minidom
import codecs

#在内存中创建一个空的文档
doc = xml.dom.minidom.Document()
print doc

#创建一个根节点company对象
root = doc.createElement('companys')

# 给根节点root添加属性
root.setAttribute('name', u'公司信息')

#将根节点添加到文档对象中
doc.appendChild(root)

# 给根节点添加一个叶子节点
company = doc.createElement('gloryroad')

# 叶子节点下再嵌套叶子节点
name = doc.createElement("Name")
name.appendChild(doc.createTextNode(u"光荣之路教育科技公司"))

# 给节点添加文本节点
ceo = doc.createElement('CEO')
ceo.appendChild(doc.createTextNode(u'吴总'))

# 将各叶子节点添加到父节点company中
company.appendChild(name)
company.appendChild(ceo)

# 然后将company添加到根节点companys中
root.appendChild(company)
print doc.toxml()

#生成xml文档
fp = codecs.open(r'C:\Users\Administrator\Documents\HBuilderProject\GetStart\xml\e5_company.xml', 'w','utf-8')
doc.writexml(fp, indent='', addindent='\t', newl='\n', encoding="utf-8")
fp.close()


