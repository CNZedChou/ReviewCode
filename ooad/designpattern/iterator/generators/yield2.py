# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  yield2.py
@Description    :  
@CreateTime     :  2021-1-10 19:53
------------------------------------
@ModifyTime     :  
"""
def foo():
    for i in range(3):
        yield i

def bar():
    generator = foo()
    yield  from generator

b = bar()
print(next(b))
print(next(b))
print(next(b))
'''
0
1
2
'''