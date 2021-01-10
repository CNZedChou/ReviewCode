# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  diamondproblem.py
@Description    :  
@CreateTime     :  2021-1-10 14:35
------------------------------------
@ModifyTime     :  
"""
class T:
    def f(self):
        print('Top')

class L(T):
    def f(self):
        print('Left')

class R(T):
    def f(self):
        print('Right')

class B(L,L):
    pass

b = B()
b.f()
print(B.mro())
'''
if B(R,L) then R's f, or L's f
[<class '__main__.B'>, <class '__main__.R'>, <class '__main__.L'>, <class '__main__.T'>, <class 'object'>]
'''
