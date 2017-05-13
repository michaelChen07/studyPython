#encoding=utf-8

#检查ipV4的有效性，有效则返回True，否则返回False

def is_ipv4(s):
	try:
		ip_list=[int(x) for x in s.split('.')]  #检查地址中是否带.，有则进行分割，无则报错
	except ValueError:
		print 'must be integer'
		return False
	print ip_list

	if len(ip_list)!=4: #判断长度是不是4
		return False
	for i in ip_list:
		if i>255 or i<0:    #判断数值的范围
			return False
		else:return True

print is_ipv4('10.211.67.21')