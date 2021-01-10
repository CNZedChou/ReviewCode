# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  coroutine.py
@Description    :  
@CreateTime     :  2021-1-10 20:58
------------------------------------
@ModifyTime     :  
"""
def coroutine(y):
    for i in range(y):
        x = yield i
        print('i=%d,x=%d'%(i,x))

c = coroutine(4)
next(c)
c.send(10)
c.send(20)
c.send(30)
