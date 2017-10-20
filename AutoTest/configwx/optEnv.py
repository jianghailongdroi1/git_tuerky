#-*- coding: utf-8 -*-
#操作环境变量
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath) #防止命令行找不到模块
formdir = os.path.dirname(os.getcwd())  # 获取上一级目录
variablePath = os.path.join(curPath, "envariable.txt")

class operateEnv:
    @staticmethod
    def set_variable(key, value):
        fd = open(variablePath, 'r')
        lines = []
        for line in fd:
            lines.append(line)
        fd.close()
        fd = open(variablePath, 'r')
        n = 0
        for i in fd.readlines():
            n += 1
            if i.split(':')[0] == key:  # 判断键重复
                if n == len(lines):
                    modify = key + ':' + value
                else:
                    modify = key + ':' + value + '\n'
                lines[n - 1] = modify  # 判断时不是以\n为判断值的，修改是需要加上
                s = "".join(lines)
                n = -1  # 标记流程的进出
                fw = open(variablePath, 'w')
                fw.write(s)
                break
        if n == len(lines):
            lines.append('\n' + key + ':' + value)  # 或者直接使用‘a’模式打开文件，追加到文件末尾
            p = "".join(lines)
            fc = open(variablePath, 'w')
            fc.write(p)

    @staticmethod
    def get_variable(key):
        fd = open(variablePath, 'r')

        for i in fd.readlines():
            if i.split(':')[0] == key:  # 判断键重复
                value = i.split(':')[1]
                break
        else:
            #value = None
            raise Exception(u"参数%s不存在！" % key)
        # print(value)
        return value


if __name__ == '__main__':
    operateEnv.set_variable('__Author__', 'mytest')

