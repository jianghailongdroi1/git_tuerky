#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
#import datetime
import logging
import logging.config


def LogAdd(Author):
        formdir = os.path.dirname(os.getcwd())
        logging.config.fileConfig(formdir + '/configwx/baseData.conf')
        return logging.getLogger(name=Author)  #生成的 日志在记录方法模块时，仅记录logger对象运行时所处的方法环境


if __name__ == '__main__':
    mylog = LogAdd('root')
    mylog.info("test")












