#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "tuerky"
# Date: 2017/10/24
import base64


class secret:
    @staticmethod
    def tosecret(key):
        #print(str(base64.b64encode(bytes(str(key), 'utf-8'))))
        return str(base64.b64encode(bytes(str(key), 'utf-8')))

    @staticmethod
    def exsecret(key):
        #print((base64.b64decode(key)).decode('utf-8'))
        return base64.b64decode(key).decode('utf-8')



if __name__ == '__main__':
    secret.tosecret('18701913175')
    #secret.tosecret('我的')
