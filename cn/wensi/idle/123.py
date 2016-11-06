#@author: chenzhen

#coding=utf-8


"""#maopao
def mp_block(L):

    for i in range(1,len(L)):
        for j in range(0,len(L)-i):
            if L[j] > L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
    return L
                
real_list=[8,93,28,39,48]
print mp_block(real_list)"""

#KUAI
def quick_block(L):
    if len(L)<=1:
        return L
    key = L[0]
    left = []
    right = []
    middle = []
    for i in range(0,len(L)):
        if L[i]>key:
            right.append(L[i])
        elif L[i]<key:
            left.append(L[i])
        elif L[i]==key:
            middle.append(L[i])
#    quick_sort(left)
#    quick_sort(right)
    return quick_block(left)+middle+quick_block(right)
real_list=[8,93,28,39,48]
print quick_block(real_list)



