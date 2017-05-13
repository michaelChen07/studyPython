#coding=utf-8
#1 图书馆可以有多本书，每本书有个作者，我需要统计一共有多少本书，有多少个作者
#2 查看所有的作者清单，和书名清单
#3 查看书名和作者的对应关系
dict_book={"hongloumeng":"caoxueqin","xiyouji":"wuchengen","shuihu":"shinaian"}

list_book=[]
list_author=[]

def get_book(t):
    return list_book

def get_author(t):
    return list_author

def count_author(t):
    for v in t.values():
        list_author.append(v)
    return len(set(t))

def count_book(t):
    for k in t:
        list_book.append(k)
    return len(t)

def get_bookandauthor(book):
    return dict_book.get(book)


print "总图书数：",count_book(dict_book)
print "图书:",get_book(dict_book)
print "总作者数：",count_author(dict_book)
print "作者:",get_author(dict_book)
print "红楼梦作者",get_bookandauthor("hongloumeng")
print "_"*50






# encode=utf-8
# 1 图书馆可以有多本书，每本书有个作者，我需要统计一共有多少本书，有多少个作者
# 2 查看所有的作者清单，和书名清单
# 3 查看书名和作者的对应关系


library_books = []


def add_book(book_name, book_author):
    book_info = {book_name: book_author}
    library_books.append(book_info)


def count_books():
    global library_books
    return len(library_books)


def count_book_author_in_library():
    global library_books
    book_author = []
    for book in library_books:
        for author in book.values():
            book_author.append(author)

    return len(list(set(book_author)))


def get_bookName_and_bookAuthor():
    global library_books
    for book in library_books:
        for book_name, book_author in book.items():
            print book_name, ":", book_author


add_book("gloryroad test1", "foster wu")
add_book("gloryroad test2", "foster wu")
add_book("gloryroad test3", "foster wu")
add_book("gloryroad test4", "Mr Li")
print library_books

print u'图书馆的藏书数量：', count_books()
print u"图书馆藏书涉及的作者数量：", count_book_author_in_library()
print u"所有图书的书名和作者信息："
get_bookName_and_bookAuthor()