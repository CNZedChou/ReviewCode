# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  mamproperty.py
@Description    :  
@CreateTime     :  2021-1-9 23:06
------------------------------------
@ModifyTime     :  
"""
class Man:
    def __init__(self,height):
        self.height = height

class Man2:
    def __init__(self,height):
        self.height = height

    @property
    def height(self):
        print('xxx')
        return self._height

    @height.setter
    def height(self,h):
        print('yyy')
        if h < 100:
            raise Exception('too short')
        elif h >250:
            raise Exception('too tall')
        self._height = h

if __name__ == '__main__':
    m = Man2(123)
    print(m.height)
    m.height = 213
    print(m.height)
    m.height = 90
    m.height = 321
