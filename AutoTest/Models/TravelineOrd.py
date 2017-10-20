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
from operation.ScreenShot import save_screenshot
from configwx.AppSetting import AppSetting
from Logging.LogConfig import LogAdd
logger = LogAdd('root')
import datetime



class travel_order:

    def __init__(self,wd):
        self.wd = wd

    def set_traveline(self):

        loc = (By.NAME, "探索")
        try:
           AppSetting.wait(self.wd,20,0.5,EC.presence_of_element_located(loc))
           element = self.wd.find_element_by_accessibility_id("探索")
           msg1 = u"探索按钮截屏"
           url1 = save_screenshot(self.wd,msg1,element)
           self.wd.find_element_by_accessibility_id("探索").click()
           msg = u"探索页截屏"
           url2 = save_screenshot(self.wd, msg)

           logger.info(u"跳转探索页面成功，截屏文件为%s%s"%(url1,url2))
        except:
            msg2 = u"探索页错误截屏"
            urlerror = save_screenshot(self.wd,msg2)
            raise Exception(u"跳转探索页错误,截屏文件为%s"%urlerror)
        self.wd.find_element_by_accessibility_id("旅游线路").click()

if __name__=='__main__':
    __Appsetting = AppSetting()
    wd = __Appsetting.stat_Appium()
    travel = travel_order(wd)
    travel.set_traveline()
