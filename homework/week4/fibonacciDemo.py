#encoding=utf-8
#打印斐波拉契数列前n项
#斐波那契数列指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,
# 特别指出：第0项是0，第1项是第一个1。从第三项开始，每一项都等于前两项之和

#获取斐波拉契数
def get_fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return get_fibonacci(n-2)+get_fibonacci(n-1)

#打印前n项
for i in xrange(10):
    print get_fibonacci(i)
