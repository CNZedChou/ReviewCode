# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  decorators.py
@Description    :  
@CreateTime     :  2021-1-9 23:24
------------------------------------
@ModifyTime     :  
"""
def steamed_milk(func):
    def decor():
        return 'Steamed milk * ' + func()
    return decor

def foamed_milk(func):
    def decor():
        return 'Foamed milk * ' + func()
    return decor

@steamed_milk
def coffee1():
    return 'Espresso'

@foamed_milk
def coffee2():
    return 'Espresso'

@steamed_milk
@foamed_milk
def coffee3():
    return 'Espresso'

def coffee():
    return 'Espresso'


@foamed_milk
@steamed_milk
def coffee5():
    return 'Espresso'

coffee4 = steamed_milk(foamed_milk(coffee))

c = coffee1()
print(c)

c = coffee2()
print(c)

c = coffee3()
print(c)

c = coffee4()
print(c)

c = coffee5()
print(c)
'''
Steamed milk * Espresso
Foamed milk * Espresso
Steamed milk * Foamed milk * Espresso
Steamed milk * Foamed milk * Espresso
Foamed milk * Steamed milk * Espresso
'''