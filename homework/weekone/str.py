#encoding=utf-8
def get_list(h,w):
    for i in xrange(1,h+1):
        for j in xrange(1,w+1):
            print "%2d\t" %(i*j),
        print

get_list(4,5)





