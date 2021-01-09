# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  property.py
@Description    :  
@CreateTime     :  2021-1-9 22:29
------------------------------------
@ModifyTime     :  
"""
class Color:
    def __init__(self,rgb_value,name):
        self.rgb_value = rgb_value
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:
            raise Exception('Invalid Name')
        self._name = name


if __name__ == '__main__':
    c = Color('#0000ff','bright read')
    print(c.name)
    c.name = 'BR'
    print(c.name)
'''
bright read
BR
'''