# -*- coding: utf-8 -*-
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from Selection.read_selection import read_selection


def execute_selection():
    selection = read_selection()
    for scriptPath in selection:
        os.system('py -3 '+scriptPath)#考虑到py2和py3的兼容性，采用兼容性命令