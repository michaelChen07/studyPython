#coding=utf-8
prompt=u"""
Welcome to Glory Road Library:
输入"图书入库",可以添加新的输入
输入"借书",可以借阅图书
输入"查库",可以借阅所有的图书名称
输入"统计册书"，可以查阅当前图书馆的图书总数
输入"退出",可以退出当前程序
"""
print prompt
books=[]
while True:
    command=raw_input("please input your command:")
    if command=="a":
        bookname=raw_input("please input book name:")
        books.append(bookname)
    elif command=="count":
        print "gloryroad library has %s books" %len(books)
    elif command=="c":
        for no,book in enumerate(books):
            print "no%s:%s " %(no,book)
    elif command=="b":
        bookname=raw_input("please input book name to borrow:")
        books.remove(bookname)  #del books[index]
    elif command=="x":
        break
    else:
        print "your command is not found,please input again!"

print "glory road library is closed now ! See u then!"
