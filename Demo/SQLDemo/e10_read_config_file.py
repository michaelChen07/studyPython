#coding=utf-8
import ConfigParser
import os

#os.chdir("D:\\Python_config")

cf = ConfigParser.ConfigParser()

cf.read("test.ini")
#cf.read("test.ini")

#return all section
secs = cf.sections()
print 'sections:', secs, type(secs)
opts = cf.options("db")
print 'options:', opts, type(opts)
kvs = cf.items("db")
print 'db:', kvs

#read by string, get读取的是字符串，getint读取的是数值
db_host = cf.get("db", "db_host")
db_port = cf.getint("db", "db_port")
db_user = cf.get("db", "db_user")
db_pass = cf.get("db", "db_password")

#read int
threads = cf.getint("concurrent", "thread")
processors = cf.getint("concurrent", "processor")
print "db_host:", db_host,type(db_host)
print "db_port:", db_port
print "db_user:", db_user
print "db_pass:", db_pass
print "thread:", threads,type(threads)
print "processor:", processors
