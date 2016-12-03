#encoding=utf-8
zoo=('elephant','parrot','penguine')
new_zoo=('tiger','snake','python',zoo)

#遍历列表中的元素，子元素在同一行显示
def get_in(n):
    for i in n:
        if isinstance(i,(tuple,list)):
            for j in i:
                print j,#将同一个元组中的数显示在一行
            print   ##将同一个元组中的数显示在一行

get_in(new_zoo)

a=[1,2,3,(4,5,6),(7,8,9),[10,11]]
get_in(a)