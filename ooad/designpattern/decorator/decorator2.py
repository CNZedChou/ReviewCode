# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  decorator2.py
@Description    :  
@CreateTime     :  2021-1-10 22:12
------------------------------------
@ModifyTime     :  
"""
def gift():
    return 'Coffee Mug'

def cushion(thickness):
    def decor(func):
        def wrapper(*args):
            return thickness * 'Cushion + '+func(*args)
        return wrapper
    return decor

def box(func):
    def wrapper(*args):
        return 'Box + ' + func(*args)
    return wrapper

def card(msg):
    def decor(func):
        def wrapper(*args):
            return 'Card [%s] + ' % msg + func(*args)
        return wrapper
    return decor


def ribbon(func):
    def wrapper(*args):
        return 'Ribbon + '+func(*args)
    return wrapper

@ribbon
@card('Don\'t worry. Be happy .- Bobby')
@box
@cushion(3)
def gift(name):
    return name

print(gift('Coffee mug'))
'''
Ribbon + Card [Don't worry. Be happy .- Bobby] + Box + Cushion + Cushion + Cushion + Coffee mug
'''
@ribbon
def gift(name):
    return name
print(gift('Coffee mug'))
'''
Ribbon + Coffee mug
'''