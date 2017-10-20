# -*- coding: utf-8 -*-
# __Author__ = tuerky
import os
import sys
from appium import webdriver

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)  # 防止命令行找不到模块
formdir = os.path.dirname(os.getcwd())  # 获取上一级目录
from Logging.LogConfig import LogAdd
logger = LogAdd('root')
from configwx.AppSetting import AppSetting
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from HTMLTestRunner import HTMLTestRunner
import unittest
from Models.Login import Login
from Models.TravelineOrd import travel_order


class MyTestSuite(unittest.TestCase):
    __AppSetting = AppSetting()  # 实例化
    wd = __AppSetting.stat_Appium()
    __Login = Login(wd)
    __travel = travel_order(wd)


    def test_Log_on(self):
        logger.info("aaaa")
        time.sleep(2)
        self.__Login.Log_on()  # 调用登录验证
        self.__travel.set_traveline()

        '''self.wd.find_element_by_accessibility_id("探索").click()
        self.wd.find_element_by_accessibility_id("旅游线路").click()
        elements = self.wd.find_elements_by_xpath(
            "//android.webkit.WebView/android.webkit.WebView[1]/android.view.View[3]")
        #print(self.wd.contexts)
        width = self.wd.get_window_size()["width"]
        height = self.wd.get_window_size()["height"]

        for i in range(11):
            n = (i * 5) + 6
            print(n)
            attr = self.wd.find_element_by_xpath(
                "//android.webkit.WebView/android.webkit.WebView[1]/android.view.View[3]/android.view.View[%d]" % n).get_attribute(
                "name")
            page1 = self.wd.page_source

            self.wd.swipe(int(width * 0.25), int(height * 0.9), int(width * 0.25), int(height * 0.3), 2000)
            time.sleep(2)


            if attr == '￥0.01起/人':
                self.wd.find_element_by_xpath(
                    "//android.webkit.WebView/android.webkit.WebView[1]/android.view.View[3]/android.view.View[%d]" % n).click()
                break
            elif i == 10:
                logger.info(u"没有0.01的价格")
                raise Exception(u"请设置0.01的产品价格！")

        self.wd.find_element_by_accessibility_id("0.01").click()
        self.wd.find_element_by_xpath(
            "//android.webkit.WebView/android.webkit.WebView[1]/android.widget.Image[3]").click()
        self.wd.find_element_by_accessibility_id("下一步").click()
        self.wd.find_element_by_accessibility_id("选择成人游客").click()
        self.wd.find_element_by_xpath("//android.webkit.WebView/android.webkit.WebView[1]/android.view.View[3]").click()
        self.wd.find_element_by_accessibility_id("提交").click()
        self.wd.find_element_by_accessibility_id("去支付").click()
        locat1 = self.wd.find_element_by_accessibility_id("微信支付")
        try:
            WebDriverWait(self.wd, 15, 0.5).until(EC.presence_of_element_located(locat1))
            self.wd.find_element_by_accessibility_id("确认支付")
        finally:
            pass
        locat2 = self.wd.find_element_by_accessibility_id("微信支付")
        try:
            WebDriverWait(self.wd, 15, 0.5).until(EC.presence_of_element_located(locat2))
            self.wd.find_element_by_accessibility_id("确认支付").click()
        except:
            if self.wd.find_element_by_accessibility_id("支付失败"):
                logger.info(u"支付失败！")
                raise Exception(u"支付失败错误")
            else:
                logger.info(u"支付超时！")
                raise Exception(u"支付超时错误！")'''


if __name__ == '__main__':
    newsuite = unittest.TestSuite()
    newsuite.addTest(MyTestSuite('test_Log_on'))
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = formdir + '\Results\\' + now + 'result.html'
    fp = open(filename, 'wb')

    # 执行测试
    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况：')
    runner.run(newsuite)
    fp.close()  # 关闭报告文件