# -*- coding: utf-8 -*-
#__Author__ = tuerky
#登录模块
import os
import sys
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)  # 防止命令行找不到模块
from configwx.AppSetting import AppSetting
from configwx.optEnv import operateEnv
from Logging.LogConfig import LogAdd
logger = LogAdd('root')
import time

class Login:
    def __init__(self,wd):
        self.wd = wd

    def Log_on(self):
        locat = (By.NAME,"我的")
        try:
           AppSetting.wait(self.wd,20,0.5,EC.presence_of_element_located(locat))
           logger.info(u"首页加载成功！")
           print("sss")
        except:
           logger.info(u"首页加载超时！")
           raise Exception(u"首页加载超时！")
        self.wd.find_element_by_accessibility_id("我的").click()
        locat1 = (By.XPATH,"//android.webkit.WebView/android.webkit.WebView[1]/android.view.View[2]/android.view.View[1]")
        try:
            AppSetting.wait(self.wd, 20, 0.5, EC.presence_of_element_located(locat1))
            logger.info(u"我的页面跳转正确")
        except:
            logger.info(u"我的页面加载超时！")
            raise Exception(u"我的页面加载超时！")
        finally:
            loginN = self.wd.find_element_by_xpath(
            "//android.webkit.WebView/android.webkit.WebView[1]/android.view.View[2]/android.view.View").get_attribute("name")
        # content-desc这个属性经过版本更新，原来是name属性所对应的，所以属性值的获取方式还是通过name的方式，如果content-desc为空则取text属性值
        if loginN == '点击登录':
            phone = operateEnv.get_variable('appuser')
            password = operateEnv.get_variable('apppassword')
            self.wd.find_element_by_xpath(
                "//android.webkit.WebView/android.webkit.WebView[1]/android.view.View[2]/android.view.View[@content-desc = \"点击登录\"]").click()
            try:
                self.wd.find_element_by_accessibility_id("手机登录").click()
                logger.info(u'登录页面跳转成功！')
            except:
                logger.info(u'登录页面跳转有误！')
                raise Exception(u"登录页面有误！")
            self.wd.find_element_by_accessibility_id("输入注册手机号").send_keys(phone)
            self.wd.find_element_by_xpath(
                "//android.webkit.WebView/android.webkit.WebView[1]/android.widget.EditText[2]").send_keys(password)
            self.wd.hide_keyboard()  # 隐藏键盘
            self.wd.find_element_by_accessibility_id("登录").click()
            locat2 = (By.NAME,"查看并编辑个人资料")
            try:
                AppSetting.wait(self.wd, 20, 0.5, EC.presence_of_element_located(locat2))
                logger.info(u"登录成功！")
            except:
                logger.info(u"登录错误！")
                raise Exception(u"登录错误！")
        else:
            logger.info(u"用户已登录！")

if __name__=='__main__':
    __Appsetting = AppSetting()
    wd = __Appsetting.stat_Appium()
    Login = Login(wd)
    Login.Log_on()


