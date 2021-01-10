# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  ducktyping.py
@Description    :  
@CreateTime     :  2021-1-10 14:03
------------------------------------
@ModifyTime     :  
"""
class Duck:
    def fly(self):
        print('Duck flying')
class Airplane:
    def fly(self):
        print('Airplane flying')

class Whale:
    def swin(self):
        print('Whale swimming')

def lift_off(entity):
    entity.fly()
duck = Duck()
airplane = Airplane()
whale = Whale()

lift_off(duck)
lift_off(airplane)
lift_off(whale)
'''
Duck flying
Airplane flying
Traceback (most recent call last):
  File "F:/GitRepository/ReviewCode/ooad/ducktyping.py", line 32, in <importmodule>
    lift_off(whale)
  File "F:/GitRepository/ReviewCode/ooad/ducktyping.py", line 25, in lift_off
    entity.fly()
AttributeError: 'Whale' object has no attribute 'fly'
'''