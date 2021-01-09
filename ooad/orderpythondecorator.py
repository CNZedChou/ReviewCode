# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  orderpythondecorator.py
@Description    :  
@CreateTime     :  2021-1-9 23:49
------------------------------------
@ModifyTime     :  
"""
def HotWater(f):
    def decor(self):
        return f(self) + ' + hot water'
    return decor

def SteamedMilk(f):
    def decor(self):
        return f(self) + ' + steamed milk'
    return decor

class Order:
    @SteamedMilk
    @HotWater
    def send(self):
        return 'espresso'

order = Order()
print(order.send())