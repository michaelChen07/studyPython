#encoding=utf-8
import subprocess
import os
class Shell(object) :
    def runCmd(self, cmd) :
        res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        # 获取子进程的标准输出，标准错误信息

        sout, serr = res.communicate()
        #sout：执行命令后的输出内容,serr出错内容,res.pid为进程编号
        return res.returncode, sout, serr, res.pid
shell = Shell()
fp = open('e22_ip.txt', 'r')
ipList = fp.readlines()
fp.close()
fp = open('e22_ping.txt', 'a')
print ipList
for i in ipList :
    i = i.strip()
    result = shell.runCmd('ping ' + i)
    if result[0] == 0 :
        w = i + ' : 0'
        fp.write(w + '\n')
    else :
        w = i + ' : 1'
        fp.write(w + '\n')
    print  result[1].decode("gbk").encode("utf-8")
fp.close()
