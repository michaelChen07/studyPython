#encoding=utf-8
import copy
def change_list(ls):
    ls[0]=18
    print"in",ls

reallist=[1,23,34,2]
copylist=copy.deepcopy(reallist)
print"out",copylist
