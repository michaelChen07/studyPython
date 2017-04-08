#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

#投保全年综合意外

driver = webdriver.Ie(executable_path="c:\\IEDriverServer")
#driver.get("http://tk.cn/")
driver.get("http://shop.tk.cn/accident/qnzh/")

#shop = driver.find_element("xpath",".//*[@id='shch_top']/div/div[3]/div/div[3]/div[3]/h4/a")
# 将鼠标悬浮到第一个链接元素上
#ActionChains(driver).move_to_element(shop).perform()
#shop.click()

#选择产品
#product = driver.find_element_by_xpath(".//*[@id='shch_top']/div/div[3]/div/div[3]/div[4]/div/div[1]/dl[1]/dd/a[1]")
#product.click()
#time.sleep(5)

#点击快速投保
button = driver.find_element_by_xpath(".//*[@id='quickBuy']")
button.click()
time.sleep(5)

#输入姓名
name = driver.find_element_by_xpath(".//*[@id='ph_name']/input")
name.send_keys(u"陈真")

#输入身份证号
id_number = driver.find_element_by_xpath(".//*[@id='ph_cid']/input")
id_number.send_keys("110101199001010023")

#输入邮箱
email = driver.find_element_by_xpath(".//*[@id='ph_email']/input")
email.send_keys("286522215@qq.com")

#输入手机号
phone = driver.find_element_by_xpath(".//*[@id='ph_mobile']/input")
phone.send_keys("17710497931")

#选择投保地区
area = driver.find_element_by_xpath(".//*[@id='applicant-area']")
area.click()
area.click()
province = driver.find_element_by_xpath(".//*[@id='area-wrap']/div[1]/ul/li[1]")
province.click()
province.click()
city = driver.find_element_by_xpath(".//*[@id='area-wrap']/div[2]/ul/li")
city.click()

#选择职业
job = driver.find_element_by_xpath(".//*[@id='pal_profession']")
job.click()

job.send_keys(Keys.ARROW_DOWN)
job.send_keys(Keys.ARROW_DOWN)#再次向下
job.send_keys(Keys.ENTER)

#勾选投保声明
select = driver.find_element_by_xpath(".//*[@id='agrChk']")
select.click()
select.click()

agree = driver.find_element_by_xpath(".//*[@id='agreeStatement_close']")
agree.click()

#点击下一步按钮
nextstep = driver.find_element_by_xpath(".//*[@id='check-form']")
nextstep.click()
nextstep.click()

#关闭浏览器
#driver.quit()