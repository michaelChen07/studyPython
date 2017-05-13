#coding=utf-8
lib = ["红楼梦","西游记","三国演义"]
print str(lib).decode('string_escape')#解决列表中中文打印显示\xe5\xb0\x8f的问题
print "支持指令：\n1 借书\n2 还书\n3 增加新书\n4 查询\n5 退出"
print "_"*30
while True:
    command=raw_input("请输入指令：")
    if command =="1":
        borrow=raw_input("请输入要借的书：")
        try:
            lib.remove(borrow)
            print "借书成功"
        except Exception,e:
            print "书名有误，请核实！"
    elif command =="2" or command == "3":
        back=raw_input("请输入要入库的书：")
        lib.append(back)
    elif command =="4":
        print str(lib).decode('string_escape')
    elif command == "5":
        break
    else:
        print "输入指令有误，请核实"

