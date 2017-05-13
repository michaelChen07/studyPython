#encoding=utf-8
n = 10
total = 0
while n > 0 :
  print "----", n
  Sex = raw_input("sex is: ")
  if Sex.strip().lower() != "f":#将性别输入的字符去掉前后不可见字符，并转换成小写
    print "unsatisfied !"
    n -= 1
    continue
  Age = int(raw_input("age is: "))
  if Age >= 10 and Age <= 12:
    print "satisfied !"
    total += 1
  else:
    print "unsatisfied !"
  n -= 1
print u"满足条件的总人数有：%s个" %total