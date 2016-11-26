# -*- coding: utf-8 -*-
import sys
def add():
    global library_books
    bookname=raw_input("please input book name to add:")
    library_books.append(bookname)

def borrow():
    bookname=raw_input("please input book name to borrow:")
    if bookname in library_books and bookname not in borrow_books.keys():
        reader_name=raw_input("please input your name to record borrow info:")
        borrow_books[bookname]=reader_name

def lend():
    global borrow_books
    bookname=raw_input("please input book name to lend:")
    while 1:
        if bookname not in borrow_books.keys():
            print "no borrow record info found!please input your book name again!"
        else:
            break
    del borrow_books[bookname]

def check():
    print " all books in library are the followings:"
    global library_books
    for i in library_books:
        print i
def exit():
    sys.exit()

print "'*'*30\nwelcome to gloryroad library*'*30\n"
print """
"add" command to add new book to library
"borrow" command to borrow book from library
"lend" command to lend book to libraay
"delete"command to delete book from library
"check" command to get all book names from library
"exit" command to quit the library system
*'*30\n
"""

library_books=[]
borrow_books={}
while 1:
    command=raw_input("please input your command:")
    exec(command+"()")
