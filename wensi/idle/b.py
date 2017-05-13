#encoding=utf-8
#冒泡


def bubble_sort(pend_list):
    for i in range(1,len(pend_list)):
        for j in range(0,len(pend_list)-i):
            if pend_list[j]>pend_list[j+1]:
                pend_list[j],pend_list[j+1]=pend_list[j+1],pend_list[j]
    return pend_list


real_l=[3,4,23,1]
print bubble_sort(real_l)
        
#深拷贝        
import copy    
def change_ls(ls):
    ls[0]=88
    print "in",ls

realls=[3,45,62,2]
copyls=copy.deepcopy(realls)
change_ls(realls)
print realls,copyls

#快排
def quick_ls(ls):
    if len(ls) <= 1:
        return ls
    key=ls[0]
    left=[]
    right=[]
    middle=[]
    for i in range(0,len(ls)):
        if ls[i] > key:
            right.append(ls[i])
        if ls[i] < key:
            left.append(ls[i])
        if ls[i] == key:
            middle.append(ls[i])
    quick_ls(left)
    quick_ls(right)
    return left+middle+right
realls=[3,45,62,2]
print quick_ls(realls)


gbk gb2312 unicode
