#encoding=utf-8

print u'''
输入a：还书；
输入b：借阅书；
输入c：显示目前所有图书；
输入x：退出程序。
'''
books = []
while True:
    x = raw_input('请输入(a、b、c、x)：'.decode('utf-8').encode('gbk'))
    if x == 'a':
        name = raw_input('请输入要还图书的名字：'.decode('utf-8').encode('gbk'))
        books.append(name)
    elif x == 'b':
        if not len(books):
            print u'对不起，图书馆里没书了。无法借阅。'
        else:
            print u'目前图书馆里有的书籍：'
            for num,book in enumerate(books):
                print "NO.%s: %s" % (num+1, book)
            name = raw_input('请输入要借图书的名字：'.decode('utf-8').encode('gbk'))
            if name not in books:
                print u'对不起，图书馆里没有您要借阅的图书。'
            else:
                books.remove(name)
                print u'借阅成功'
    elif x == 'c':
        print u'目前图书馆里有的书籍：'
        for num,book in enumerate(books):
            print "NO.%s: %s" % (num+1, book)
    elif x == 'x':
        print u'退出'
        break
    else:
        print u'输入有误，请重新输入'
