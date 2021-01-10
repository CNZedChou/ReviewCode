# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  infinateiter.py
@Description    :  
@CreateTime     :  2021-1-10 18:09
------------------------------------
@ModifyTime     :  
"""
import random
class RandomIterator:
    def __init__(self,n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        return random.randint(0,self.n)

r = RandomIterator(56)
print(next(r))
print(next(r))
print(next(r))
'''
2
21
49
'''
