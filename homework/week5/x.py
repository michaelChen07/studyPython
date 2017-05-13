#encoding=utf-8
import re

phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print "电话号码是: ", num

# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print "电话号码是 : ", num


# 将匹配的字符串中的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))

#匹配ip
rule = r"\d{3}[.]\d{3}[.]\d{1,3}[.]\d{1,3}"
def get_pattern(rule,string):
    result = re.search(rule,string).group()
    if result:
        print result
        return result
    else:
        print "not found"
        return None

if __name__=="__main__":
    assert get_pattern(rule, "192.168.1.0") == "192.168.1.0"
    assert get_pattern(rule, "192.168.255.255") == "192.168.255.255"




