# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  mro.py
@Description    :  
@CreateTime     :  2021-1-10 14:55
------------------------------------
@ModifyTime     :  
"""
class T:
    def f(self):
        print('Top')

class L(T):
    def f(self):
        print('Left')
        super().f()

class R(T):
    def f(self):
        print('Right')
        super().f()

class B(L,R):
    def f(self):
        print('Bottom')
        super().f()

b = B()
b.f()
print(B.mro())