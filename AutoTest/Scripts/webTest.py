# -*- coding: utf-8 -*-
# __Author__ = tuerky
from selenium import webdriver
from Logging.LogConfig import LogAdd
logger = LogAdd('root')
import re


page = 'indexx = "5",indexx = "90",indexx = "11",indexx = "23"'
r = re.findall(r'index = "(\d+)"',page)
print(r)





#browser = webdriver.Chrome()
#browser.get('https://www.baidu.com')

#browser = webdriver.Chrome()
#browser.get('https://www.baidu.com')
#browser.maximize_window()
#browser.find_element_by_id("kw").send_keys(u"国资商城")
#browser.find_element_by_id("su").click()
#browser.find_element_by_name("tj_login").click()
#browser.find_element_by_xpath("//*[text()=\"更多产品\"]").click()
#browser.find_element_by_link_text("更多产品").click()
#browser.find_element_by_xpath("//*[@class=\"bdmainlink\"]/div[@class=\"bdbriimgtitle\"]").click()





#xpath
#id
#name
#模糊定位"//*[contains(@href,'sso/login/')]")
#text定位
#多标签定位 and
