#-*- coding: utf-8 -*-
#屏幕截屏
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath) #防止命令行找不到模块
formdir = os.path.dirname(os.getcwd())  # 获取上一级目录
from PIL import Image
import datetime
nowTime = datetime.datetime.now().strftime('%Y-%m-%d')
delTime = datetime.datetime.now().strftime('%H_%M_%S')

def save_screenshot(browser,msg=str,element = None):
    if os.path.exists(os.path.join(formdir, "screenshot\sh%s"%nowTime)):
        pass
    else:
        os.mkdir(os.path.join(formdir, "screenshot\sh%s"%nowTime))
    variablePath = (formdir + "\screenshot\sh%s\%s%s.png"%(nowTime,msg,delTime))
    browser.get_screenshot_as_file(variablePath)
    if element:
        beg = element.location
        size = element.size
        start_x = beg['x']
        start_y = beg['y']
        end_x = start_x + size['width']
        end_y = start_y + size['height']
        box = (start_x,start_y,end_x,end_y)
        name = str(start_x) + '_'+ str(start_y) + '_'+ str(end_x) + '_' + str(end_y)
        image = Image.open(variablePath)
        newimage = image.crop(box)
        newPath = os.path.join(formdir, "screenshot\sh%s\%s%s%s.png"%(nowTime,delTime,msg,name))
        newimage.save(newPath)
        os.popen('del %s'%variablePath)
        return newPath
    else:
        return variablePath









