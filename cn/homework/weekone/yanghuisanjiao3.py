#encoding=utf-8
def yang_hui(n):
   num=[1]
   i=0
   while i<n:
      print ' '*((2*n-1)-2*(i-1))+' '.join("%4s"%x for x in num)
      #num.append(1)
      num=[1]+[num[x]+num[x+1] for x in range(len(num)-1)]+[1]
      i+=1
yang_hui(11)
