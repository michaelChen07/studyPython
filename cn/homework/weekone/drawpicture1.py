#encoding=utf-8
def draw_pic(n):
    for i in range(1,n+1):
        if i == 1 or i==n:
            print " "*10+"*"
        elif i==2 or i==n-1:
            print " "*5+"*"+" "*5+"*"
        elif i>3 and i<n-1:
            print "*"
draw_pic(10)


