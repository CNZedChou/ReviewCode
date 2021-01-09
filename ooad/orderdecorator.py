# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  orderdecorator.py
@Description    :  
@CreateTime     :  2021-1-9 23:36
------------------------------------
@ModifyTime     :  
"""
class Order:
    def send(self):
        return 'espresso'

class HotWater:
    def __init__(self,order):
        self.order = order

    def send(self):
        return self.order.send()+ ' + hot water'

class SteamedMilk:
    def __init__(self,order):
        self.order = order

    def send(self):
        return self.order.send()+ ' + steamed milk'

class BrownSugar:
    def __init__(self,order):
        self.order = order

    def send(self):
        return self.order.send()+' + brown sugar'

if __name__ == '__main__':
    order = Order()
    print(order.send())

    order2 = HotWater(order)
    print(order2.send())

    order3 = SteamedMilk(HotWater(order))
    print(order3.send())

    order4 = BrownSugar(SteamedMilk(order))
    print(order4.send())