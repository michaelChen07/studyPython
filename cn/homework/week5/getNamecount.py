#encoding=utf-8

#统计名字列表中，各名字的首字母在名字列表中出现的次数
name_list=["wang","zhao","marry","lucy","lily"]

#获取首字母，放入列表
def get_list(L):
    result_list=[]
    for i in L:
        result_list.append(i[0])
    return result_list

#每个首字母出现的次数
def get_count(s):
    dic_name={}
    for j in s:
        dic_name[j]=s.count(j)
    return dic_name

print get_count(get_list(name_list))