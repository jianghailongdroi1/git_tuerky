#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import socket
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)  # 防止命令行找不到模块
formdir = os.path.dirname(os.getcwd())  # 获取上一级目录
variPath = os.path.join(curPath,'baseData.conf')
logpath = os.path.join(formdir,'Logging\\DateLog\\log.log')
from appium import webdriver
import subprocess
import time
import configparser
from selenium.webdriver.support.ui import WebDriverWait
from Logging.LogConfig import LogAdd
logger = LogAdd('root')


class AppSetting:
    __configParser = configparser.ConfigParser()  # 实例化对象


    def __init__(self):
        self.__configParser.read(variPath)

    def port_in_use(self,host,port):   #判断端口是否使用
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((host,int(port)))
            s.shutdown(2)
            logger.info(u'%s端口被占用' % port)
            return True
        except:
            logger.info(u'%s端口未使用' % port)
            return False

    def stat_Appium(self):
        host = self.__configParser.get('appsetting','host')
        port = self.__configParser.get('appsetting','port')
        apiversion = self.__configParser.get('appsetting','apiversion')
        platform = self.__configParser.get('appsetting', 'platform_name')
        version = self.__configParser.get('appsetting', 'version')
        dev = self.__configParser.get('appsetting', 'dev')
        path = self.__configParser.get('appsetting', 'path')
        cmd = 'start /b appium --address %s --port %s --app %s ' \
              '--platform-name %s --platform-version %s --automation-name Appium --log-no-color'%(host,port,path,platform,apiversion)
        if self.port_in_use(host, port):
            os.system('taskkill /f /t /im node.exe')     #杀进程
        p = subprocess.call(cmd, shell=True, stdout=open(logpath, 'w'),   #打开进程
                                stderr=subprocess.STDOUT)

        time.sleep(2)
        PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))
        desired_caps = {}
        desired_caps['platformName'] = platform
        desired_caps['platformVersion'] = version
        desired_caps['deviceName'] = dev
        # 'huawei-huawei_mt7_tl00-P4M7N15320035581'
        desired_caps['app'] = PATH(path)  # 可以使用activity 和package定位
        return webdriver.Remote('http://%s:%s/wd/hub' % (host, port), desired_caps)



    @staticmethod
    def wait(browser, timeout, poll_frequency, func):
        WebDriverWait(browser, timeout, poll_frequency).until(func)


if __name__ == '__main__':

    __AppSetting = AppSetting()
    __AppSetting.port_in_use('127.0.0.1','4723')
    #__AppSetting.stat_Appium()

