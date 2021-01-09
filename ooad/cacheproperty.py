# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  cacheproperty.py
@Description    :  
@CreateTime     :  2021-1-9 22:31
------------------------------------
@ModifyTime     :  
"""
import time
from urllib.request import urlopen

class WebPage:
    def __init__(self,url):
        self.url = url
        self._content = None

    @property
    def content(self):
        if not self._content:
            print('get new page')
            self._content = urlopen(self.url).read()
        return self._content

if __name__ == '__main__':
    webpage = WebPage('http://www.baidu.com/')
    print(webpage.content)
    print(webpage.content)