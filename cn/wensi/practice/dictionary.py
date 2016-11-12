#encoding=utf-8
dica = {"find":"look for","good":"do sth well"}
print dica
print "you can input command : add,check,del,bye"

#print dica
while True:
    command = raw_input("please input command:")
    if command == "add":
        word = raw_input("please input the word you want to add:")
        mean = raw_input("please input the word's mean:")
        if word in dica:
            print "sorry,the word is exist"
        else:
            dica[word] = mean
            print "sucessful",dica
    elif command == "check":
        word = raw_input("please input the word you want to check:")
        if word not in dica:
            print "sorry,the word not exist"
        else:
            print dica[word]
    elif command == "del":
        word = raw_input("please input the word you want to del:")
        if word in dica:
            del dica[word]
            print "sucessful",dica
        else:
            print "sorry,the word is not exist"
    elif command =="bye":
        print "goodbye"
        break
    else:
        print "something is wrong,please try again!"