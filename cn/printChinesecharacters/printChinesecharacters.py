#encoding=utf-8
#解决中文打印显示\xe5\xb0\x8f的问题

dict_book={"红楼梦":"曹雪芹","西游记":"吴承恩","水浒":"施耐庵"}
print str(dict_book).decode('string_escape')

lib = ["红楼梦","西游记","三国演义"]
print str(lib).decode('string_escape')#解决列表中中文打印显示\xe5\xb0\x8f的问题