#encoding=utf-8

import xml.dom.minidom
from xml.dom.minidom import parse
#minidom解析器打开xml文档并将其解析为内存中的一棵树
DOMTree = parse(r"C:\Users\Administrator\Documents\HBuilderProject\GetStart\xml\e2_book.xml")

#获取xml文档对象，就是拿到树的根
booklist = DOMTree.documentElement

if booklist.hasAttribute("type") :
  #判断根节点booklist是否有type属性，有则获取并打印属性的值
    print u"Root element is", booklist.getAttribute("type")

#获取booklist对象中所有book节点的list集合
books = booklist.getElementsByTagName("book")
print u"book节点的个数：", books.length

for book in books :
    print "*******************book*******************"
    if book.hasAttribute("category") :
        print u"category is", book.getAttribute("category")

  #根据结点名title拿到这个book结点下所有的title结点的集合list。
  #[0]表示第一个title标签，因为一个<book>...</book>之间可能会
  #定义多个title标签
    title = book.getElementsByTagName('title')[0]
    print "Title is", title.childNodes[0].data
    author = book.getElementsByTagName('author')[0]
    print "author is", author.childNodes[0].data
    pageNumber = book.getElementsByTagName('pageNumber')[0]
    print "pageNumber is", pageNumber.childNodes[0].data
