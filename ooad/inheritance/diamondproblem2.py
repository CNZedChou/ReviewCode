# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  diamondproblem2.py
@Description    :  
@CreateTime     :  2021-1-10 14:40
------------------------------------
@ModifyTime     :  
"""
class T:
    def f(self):
        print('Top')

class L(T):
    def f(self):
        print('Left')
        T.f(self)

class R(T):
    def f(self):
        print('Right')
        T.f(self)

class B(L,R):
    def f(self):
        print('Bottom')
        L.f(self)
        R.f(self)

b = B()
b.f()
'''
Bottom
Left
Top
Right
Top
'''