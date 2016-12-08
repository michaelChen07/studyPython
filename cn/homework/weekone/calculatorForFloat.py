#encoding=utf-8
#字典进行简化，相当于switch
a=float(input("please input a number:"))
while 1:#符合条件，一直执行循环
    b=raw_input("please input an operator:")
    c=float(input("please input a number:"))
    result={
        "+":a+c,
        "-":a-c,
        "*":a*c,
        "/":a/c
        }
    a=result.get(b)
    print a