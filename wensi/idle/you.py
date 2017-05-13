# -*- coding: utf-8 -*-
#冒泡
def maop_block(pend_list):
    if type(pend_list).__name__!="list" and type(pend_list).__name__!="tuple":
        print"please input a list or tuple"
        return
    if len(pend_list)<=1:
        return pend_list
    if type(pend_list).__name__=="tuple":
        list(pend_list)
    for i in range(1,len(pend_list)):
        for j in range(0,len(pend_list)-i):
            if pend_list[j]>pend_list[j+1]:
                pend_list[j],pend_list[j+1]=pend_list[j+1],pend_list[j]
    return pend_list
L=[3,9,41,42,5]
print maop_block(L)
    
    
#快排
def quick_b(L):
    if len(L)<=1:
        return L
    key=L[0]
    left=[]
    right=[]
    middle=[]
    for i in range(0,len(L)):
        if L[i]>key:
            right.append(L[i])
        elif L[i]<key:
            left.append(L[i])
        else:
            middle.append(L[i])
    return quick_b(left)+middle+quick_b(right)

L=[3,9,41,42,5]
print quick_b(L)
        
print "*"*20
import copy
def change_list(ls):
    ls[0]=18
    print"in",ls

reallist=[1,23,34,2]
copylist=copy.deepcopy(reallist)
print"out",copylist
