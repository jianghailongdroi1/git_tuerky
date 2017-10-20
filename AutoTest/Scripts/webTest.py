# -*- coding: utf-8 -*-
# __Author__ = tuerky
from selenium import webdriver


browser = webdriver.Chrome()
browser.get('https://www.baidu.com')

#browser = webdriver.Chrome()
#browser.get('https://www.baidu.com')
browser.maximize_window()
#browser.find_element_by_id("kw").send_keys(u"国资商城")
#browser.find_element_by_id("su").click()
#browser.find_element_by_name("tj_login").click()
browser.find_element_by_xpath("//*[text()=\"更多产品\"]").click()
#browser.find_element_by_link_text("更多产品").click()
#browser.find_element_by_xpath("//*[@class=\"bdmainlink\"]/div[@class=\"bdbriimgtitle\"]").click()





#xpath
#id
#name
#模糊定位"//*[contains(@href,'sso/login/')]")
#text定位
#多标签定位 and
