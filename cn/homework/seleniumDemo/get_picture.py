#encoding=utf-8
#ie\chrome\firefox三种浏览器下，分别截图baidu\sogou\youdao，保存在当前日期的目录下。网址要保存在某个数据文件中

from selenium import webdriver
import os
import time
import re

#创建文件保存的目录
def creat_dir():
    today = time.strftime("%Y%m%d",time.localtime())
    os.chdir(os.getcwd())
    try:
        os.mkdir(today)
    except Exception,e:
        print "exist!"
    return os.getcwd()+"\\"+today


#访问网址并截图
def get_pictures(browser_name,url):

    if browser_name == "ie":
        driver = webdriver.Ie(executable_path="C:\\IEDriverServer")
    elif browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="C:\\geckodriver")

    driver.get(url)
    time.sleep(3)
    driver.maximize_window()

    picturepath = creat_dir()+"\\"+browser_name+"_"+re.search(r"http://www\.(\w+)\..*",url).group(1)+".png"
    driver.get_screenshot_as_file(picturepath)

    driver.quit()

if __name__=="__main__":
    browser_list = ["ie","firefox"]
    #browser_list = ["chrome"]

    for browset_name in browser_list:
        urlpath = "urllist.txt"
        with open(urlpath,"r") as f:
            for line in f:
                url = line.strip()
                get_pictures(browset_name,url)
