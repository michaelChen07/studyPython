# encoding=utf-8

from Book import *

print u"欢迎光临"
hongloumeng = Book("红楼梦", "曹雪芹")
xiyouji = Book("西游记", "吴承恩")
sanguoyanyi = Book("三国演义", "施耐庵")
books = [hongloumeng, xiyouji, sanguoyanyi]

while True:
    print u"请输入您要进行的操作，目前支持的操作：" \
          u"1. 图书入库 " \
          u"2. 统计册数  " \
          u"3. 查库 " \
          u"4. 借书 " \
          u"5. 退出 "

    command = input()
    if command == 1:
        name = raw_input("请输入您要入库的书名：")
        author = raw_input("请输入您要入库的作者：")
        books.append(Book(name, author))
        print "成功入库"
    elif command == 2:
        print u"图书馆共有 %s 本图书" % len(books)
        print u"分别是："
        for no, book in enumerate(books):
            print "no%s:%s, %s " % (no+1, book.name, book.author)
    elif command == 3:
        for no, book in enumerate(books):
            print "no%s:%s, %s " % (no+1, book.name, book.author)
    elif command == 4:
        print u"下列书籍可借："
        for no, book in enumerate(books):
            print "no%s:%s, %s " % (no+1, book.name, book.author)
        index = input("请输入删除数目序号（1, 2, 3）：")
        try:
            books.remove(books[index-1])
            print u'借书成功！'
        except Exception, e:
            print u'抱歉该书不存在！'
    elif command == 5:
        print u"谢谢光临"
        break
    else:
        print u"您的指令输入有误，请重新输入"

