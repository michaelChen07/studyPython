#encoding=utf-8
from selenium import webdriver
import time
import datetime
import os
import re

#截图并保存在文件夹中
def creat_dir_by_date_time():
    today = datetime.date.today()
    print "today:",str(today)
    if not os.path.exists("d:\\"+str(today)):
        os.mkdir("d:\\"+str(today))
    return "d:\\"+str(today)

def creat_url_list_file():
    with open("d:\\urllist.txt","w") as f:
        f.write("http://www.sogou.com\n")
        f.write("http://www.baidu.com\n")
        f.write("http://www.youdao.com\n")

def capture_url_image_by_browser(browser_name,url):
    if browser_name == "ie":
        drive = webdriver.Ie(executable_path="C:\\IEDriverServer")
    elif browser_name == "chrome":
        drive = webdriver.Chrome(executable_path="C:\\chromedriver")
    else:
        drive = webdriver.Firefox(executable_path="C:\\geckodriver")

    drive.get(url)
    picpath = creat_dir_by_date_time()+"\\"+browser_name+"_"+re.search(r"http://www\.(\w+)\..*",url).group(1)+".png"
    drive.get_screenshot_as_file(picpath)

    drive.quit()

if __name__=="__main__":
    creat_dir_by_date_time()
    #creat_url_list_file()
    #capture_url_image_by_browser("ie","http://www.sogou.com")
    browser_list = ["ie","chrome","firefox"]

    for browset_name in browser_list:
        with open("d:\\urllist.txt") as f:
            for line in f:
                url = line.strip()
                capture_url_image_by_browser(browset_name,url)

