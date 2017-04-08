#encoding=utf-8
import ConfigParser
import os

#读取配置文件的方法

configFilePath=os.path.dirname(os.path.abspath(__file__))\
                            + "\\UiObjectMap.ini"
print "path:",configFilePath

cf = ConfigParser.ConfigParser()
cf.read(configFilePath)

print cf.sections()
print cf.options("gloryroad")
dbname = cf.get("gloryroad","dbname")
username = cf.get("gloryroad","username")
password = cf.get("gloryroad","password")


webserver= cf.get("web","webserver")

print dbname
print username
print password

print webserver