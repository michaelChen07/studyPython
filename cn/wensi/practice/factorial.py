#encoding=utf-8
sum_people = 0
for i in range(10):

    sex = raw_input("please input your sex (f or m):")
    if sex == "m":
        print "sorry,we can not play together!"
        continue
    elif sex == "f":
        age = int(raw_input("please input your age:"))
        if age >=10 and age <= 12:
            print "welcome to join our football team!"
            sum_people += 1
        else:
            print "sorry!"
    else:
        print "your input sex is wrong , please reinput!"
        continue

print "our football team has %d members!" %sum_people

