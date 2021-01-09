# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  articleproperty.py
@Description    :  
@CreateTime     :  2021-1-9 22:36
------------------------------------
@ModifyTime     :  
"""
class Article:
    def __init__(self,name):
        self.name = name
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @likes.setter
    def likes(self,newlikes):
        if not newlikes:
            raise Exception('Error')
        self._likes = newlikes

if __name__ == '__main__':
    a = Article('aid')
    print(a.likes)
    a.likes = a.likes + 1
    print(a.likes)

'''
0
1
'''