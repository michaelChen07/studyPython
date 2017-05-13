#encoding=utf-8
def if_sriangle(a,b,c):
    long = max(a,b,c)
    if (a+b+c > 2*long):
        return "sriangle"
    else:
        return "not a sriangle"
print if_sriangle(1,1,0)
