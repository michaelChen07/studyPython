#encoding=utf-8
print u"欢迎光临"
books=["红楼梦","西游记","三国演义"]
while True:
    print u"请输入您要进行的操作，目前支持的操作：图书入库、借书、查库、统计册数、退出"
    command=raw_input()
    if command=="图书入库".decode("utf-8").encode("gbk"):
        bookname=raw_input("请输入您要入库的书名：".decode("utf-8").encode("gbk"))
        books.append(bookname)
    elif command=="统计册数".decode("utf-8").encode("gbk"):
        print u"图书馆共有 %s 本图书" %len(books)
    elif command=="查库".decode("utf-8").encode("gbk"):
        for no,book in enumerate(books):
            print "no%s:%s " %(no,book)
    elif command=="借书".decode("utf-8").encode("gbk"):
        name=raw_input("请输入书名：".decode("utf-8").encode("gbk"))
        try:
            books.remove(name)
            print u'借书成功！'
        except Exception,e:
            print u'抱歉该书不存在！' 
    elif command=="退出".decode("utf-8").encode("gbk"):
        print u"谢谢光临"
        break
    else:
        print u"您的指令输入有误，请重新输入"

    

