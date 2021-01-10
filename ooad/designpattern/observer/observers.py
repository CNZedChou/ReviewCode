# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  observers.py
@Description    :  
@CreateTime     :  2021-1-10 21:21
------------------------------------
@ModifyTime     :  
"""
class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def attach(self,observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._product

    @product.setter
    def product(self,value):
        self._product = value
        self._update_observers()

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self,value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
        for o in self.observers:
            o()

class ConsoleObserver:
    def __init__(self,inventory):
        self.inventory = inventory

    def __call__(self):
        print(self.inventory.product)
        print(self.inventory.quantity)

class UnitedKingdomObserver(ConsoleObserver):
    def __call__(self):
        print('Observer from Britain')
        print(self.inventory.product)
        print(self.inventory.quantity)

class UnitedStatesObserver(ConsoleObserver):
    def __call__(self):
        print('Observer from America')
        print(self.inventory.product)
        print(self.inventory.quantity)

if __name__ == '__main__':
    i = Inventory()
    uk_observer = UnitedKingdomObserver(i)
    i.attach(uk_observer)
    us_observer = UnitedStatesObserver(i)
    i.attach(us_observer)
    i.product = 'E45'
    i.quantity = 2
'''
Observer from Britain
E45
0
Observer from America
E45
0
Observer from Britain
E45
2
Observer from America
E45
2
'''