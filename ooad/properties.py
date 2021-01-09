# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  properties.py
@Description    :  
@CreateTime     :  2021-1-9 22:24
------------------------------------
@ModifyTime     :  
"""
class Color:
    def __init__(self,rgb_value,name):
        self.rgb_value = rgb_value
        self._name = name

    def _set_name(self,name):
        if not name:
            raise Exception("Invalid Name")
        self._name = name

    def _get_name(self):
        return self._name

    name = property(_get_name,_set_name)


if __name__ == '__main__':
    c = Color('#0000ff','bright read')
    print(c.name)
    c.name = 'BR'
    print(c.name)
'''
bright read
BR
'''