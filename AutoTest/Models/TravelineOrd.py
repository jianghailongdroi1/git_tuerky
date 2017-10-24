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
from configwx.optEnv import operateEnv
from operation.ScreenShot import save_screenshot
from configwx.AppSetting import AppSetting
from Logging.LogConfig import LogAdd
tralogger = LogAdd('root')
import time
import re
from configwx.baenCode import secret


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

           tralogger.info(u"跳转探索页面成功，截屏文件为%s%s"%(url1,url2))
        except:
            msg2 = u"探索页错误截屏"
            urlerror = save_screenshot(self.wd,msg2)
            tralogger.info(u"跳转探索页错误,截屏文件为%s"%urlerror)
            raise Exception(u"跳转探索页错误,截屏文件为%s"%urlerror)

        self.wd.find_element_by_accessibility_id("旅游线路").click()
        time.sleep(2)
        page1 = self.wd.page_source
        r = re.findall(
            r'index="(\d+)" text="" class="android.view.View" package="com.gznb.xl" content-desc="￥0.01起/人"', page1)  #正则匹配index，可以计算下拉坐标
        if r == []:
            tralogger.info(u"没有起价为0.01的旅游订单")
            raise Exception(u"没有起价为0.01的旅游订单")
        else:
            pass
        total = int(float(r[0])/5)  #根据index处理成第几个订单
        tralogger.info(u"选择第%s个旅游项目下订单"%total)
        width = self.wd.get_window_size()["width"]
        height = self.wd.get_window_size()["height"]
        for i in range(total):
           self.wd.swipe(int(width * 0.25), int(height * 0.9), int(width * 0.25), int(height * 0.3), 2000) #下滑到元素可见位置

        loc1 = (By.NAME, "￥0.01起/人")
        try:
            AppSetting.wait(self.wd,20,0.5,EC.presence_of_element_located(loc1))
            msg3 = u"旅游订单成功截屏截屏"
            url3 = save_screenshot(self.wd,msg3)
            tralogger.info(u"旅游订单定位成功，截屏文件为%s"%url3)
        except:
            msg4 = u"旅游订单失败截屏截屏"
            urlerror1 = save_screenshot(self.wd,msg4)
            tralogger.info(u"旅游订单没有获取成功,截屏文件为%s"%urlerror1)
            raise Exception(u"旅游订单没有获取成功,截屏文件为%s"%urlerror1)
        self.wd.find_element_by_accessibility_id("￥0.01起/人").click()
        loc2 = (By.NAME, "0.01")
        try:
            AppSetting.wait(self.wd,10,0.5,EC.presence_of_element_located(loc2))
            LineName = self.wd.find_element_by_xpath(
                "//android.webkit.WebView/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]").get_attribute("name") #获取旅游订单名称
            msg5 = u"%s 旅游项目截屏"%LineName
            url4 = save_screenshot(self.wd,msg5)
            tralogger.info(u"%s 项目打开成功，截屏文件为%s"%(LineName, url4))
        except:
            msg6 = u"旅游项目打开失败截屏"
            url5 = save_screenshot(self.wd,msg6)
            tralogger.info(u"旅游项目打开失败，截屏文件为%s"%url5)
            raise Exception(u"旅游项目打开失败，截屏文件为%s"%url5)
        self.wd.find_element_by_accessibility_id("0.01").click()
        location = (By.NAME,"手机登录")
        try:
           AppSetting.wait(self.wd, 10, 0.5, EC.presence_of_element_located(location))
           #__login = Login(self.wd) #内部实例化
           #__login.Log_on() #调用登录模块
           phone = operateEnv.get_variable('appuser')
           password = operateEnv.get_variable('apppassword')
           self.wd.find_element_by_accessibility_id("输入注册手机号").send_keys(phone)
           self.wd.find_element_by_xpath(
               "//android.webkit.WebView/android.webkit.WebView[1]/android.widget.EditText[2]").send_keys(password)
           self.wd.hide_keyboard()  # 隐藏键盘
           self.wd.find_element_by_accessibility_id("登录").click()
        except:
            tralogger.info(u"用户已登录！")
            pass

        loc3 = (By.NAME, "价格说明")
        try:
            AppSetting.wait(self.wd,10,0.5,EC.presence_of_element_located(loc3))
            msg7 = u"旅游订单可定天数截屏"
            url6 = save_screenshot(self.wd,msg7)
            tralogger.info(u"%s"%url6)
        except:
            msg8 = u"旅游订单可定天数页面打开失败截屏"
            urlerror2 = save_screenshot(self.wd,msg8)
            tralogger.info(u"%s"%urlerror2)
            raise Exception(u"%s"%urlerror2)
        self.wd.find_element_by_xpath(
            "//android.webkit.WebView/android.webkit.WebView[1]/android.widget.Image[3]").click()
        self.wd.find_element_by_accessibility_id("下一步").click()
        loc4 = (By.NAME, "去支付")
        try:
            AppSetting.wait(self.wd,10,0.5,EC.presence_of_element_located(loc4))
            msg8 = u"旅游订单填写信息截屏"
            url7 = save_screenshot(self.wd,msg8)
            tralogger.info(u"填写信息页面打开成功，截屏文件：%s"%url7)
        except:
            msg9 = u"旅游订单填写信息失败截屏"
            urlerror3 = save_screenshot(self.wd,msg9)
            tralogger.info(u"旅游订单填写信息失败,截屏文件：%s"%urlerror3)
            raise Exception(u"旅游订单填写信息失败,截屏文件：%s"%urlerror3)
        self.wd.find_element_by_accessibility_id("选择成人游客").click()
        loc5 = (By.NAME, "选择成人游客")
        try:
            AppSetting.wait(self.wd,10,0.5,EC.presence_of_element_located(loc5))
            msg10 = u"旅游订单选择游客页面截屏"
            url8 = save_screenshot(self.wd,msg10)
            tralogger.info(u"旅游订单选择游客页面打开成功,截屏文件:%s"%url8)
        except:
            msg11 = u"旅游订单选择游客页面失败截屏"
            urlerror4 = save_screenshot(self.wd,msg11)
            tralogger.info(u"旅游订单选择游客页面失败,截屏文件为：%s" % urlerror4)
            raise Exception(u"旅游订单选择游客页面失败,截屏文件为：%s" % urlerror4)
        self.wd.find_element_by_xpath(
            "//android.webkit.WebView/android.webkit.WebView[1]/android.view.View[3]").click()
        self.wd.find_element_by_accessibility_id("提交").click()
        time.sleep(0.5)
        self.wd.find_element_by_accessibility_id("去支付").click()
        loc6 = (By.NAME, "微信支付")
        try:
            AppSetting.wait(self.wd,15,0.5,EC.presence_of_element_located(loc6))
            msg12 = u"在线支付页成功截屏"
            url9 = save_screenshot(self.wd,msg12)
            tralogger.info(u"在线支付页打开成功，截屏文件：%s"%url9)
        except:
            msg13 = u"在线支付页失败截屏"
            urlerror5 = save_screenshot(self.wd,msg13)
            tralogger.info(u"在线支付页打开失败，截屏文件：%s"%urlerror5)
            raise Exception(u"在线支付页打开失败，截屏文件：%s"%urlerror5)
        self.wd.find_element_by_accessibility_id("微信支付").click()
        self.wd.find_element_by_accessibility_id("确认支付").click()
        loc7 = (By.NAME, "微信号/QQ/邮箱登录")
        # noinspection PyBroadException
        try:
            AppSetting.wait(self.wd, 8, 0.5, EC.presence_of_element_located(loc7))
            msg14 = u"跳转微信登录页成功截屏"
            url10 = save_screenshot(self.wd,msg14)
            tralogger.info(u"跳转微信登录页成功截屏文件：%s" % url10)
            wxuser = operateEnv.get_variable('wxuser')
            wxpassword = operateEnv.get_variable('wxpassword')
            self.wd.find_element_by_name("请填写微信号/QQ号/邮箱").send_keys(wxuser)
            self.wd.find_element_by_xpath(
                "//android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.EditText").send_keys(wxpassword)
            self.wd.find_element_by_name("登录").click()

        except:
            loc8 = (By.NAME, "立即支付")
            try:
                AppSetting.wait(self.wd, 15, 0.5, EC.presence_of_element_located(loc8))
            except:
                msg15 = u"支付异常截屏"
                urlerror6 = save_screenshot(self.wd, msg15)
                tralogger.info(u"支付异常！截屏文件：%s" % urlerror6)
                raise Exception(u"支付异常，截屏文件：%s" % urlerror6)
            else:
                pass

        finally:
            loc9 = (By.NAME, "立即支付")
            try:
               AppSetting.wait(self.wd, 15, 0.5, EC.presence_of_element_located(loc9))
            except:
               msg17 = u"打开微信后支付超时截屏"
               urlerror8 = save_screenshot(self.wd,msg17)
               tralogger.info(u"微信端返回支付超时，截屏文件为：%s" % urlerror8)
               raise Exception(u"微信端返回支付超时，截屏文件为：%s" % urlerror8)

        self.wd.find_element_by_name("立即支付").click()
        time.sleep(2)
        wxpaypass = operateEnv.get_variable('wxpaypassword')
        self.wd.find_element_by_xpath(
            "//android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[2]/android.widget.RelativeLayout").send_keys(wxpaypass)
        time.sleep(1)
        msg18 = u"微信支付成功"
        url18 = save_screenshot(self.wd, msg18)
        tralogger.info(u"微信支付成功,截屏文件为：%s" % url18)
        self.wd.find_element_by_name("返回行理").click()
        time.sleep(2)
        msg19 = u"支付成功"
        url19 = save_screenshot(self.wd, msg19)
        tralogger.info(u"支付成功，截屏文件：%s" % url19)
        self.wd.find_element_by_accessibility_id("确定").click()
        time.sleep(1)
        ltod = self.wd.find_element_by_xpath("//android.webkit.WebView/android.webkit.WebView[1]/android.view.View[5]").get_attribute("name")
        applinorder = str(ltod).split("：")[1]
        operateEnv.set_variable('applinorder', applinorder)








































if __name__=='__main__':

    __Appsetting = AppSetting()
    wd = __Appsetting.stat_Appium()
    travel = travel_order(wd)
    travel.set_traveline()
