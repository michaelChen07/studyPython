#encoding=utf-8
import os
import time
starttime = time.time()

today = time.strftime("%Y%m%d",time.localtime())
list_file = os.listdir(r"d:\test\test2")

for i in list_file:
    path = os.path.join("d:\\test\\test2",i)

    if os.path.isfile(path):
        creattime = time.localtime(os.path.getctime(path))

        if time.strftime("%Y%m%d",creattime) == today:
            with open(path,"w") as fp:
                fp.write(path+"\n")
                fp.write(str(os.path.splitext(path)))
        else:
            os.remove(path)

endtime = time.time()
print "costtime:",endtime-starttime




