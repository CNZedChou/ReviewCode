# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  splitmethod.py
@Description    :  
@CreateTime     :  2021-1-15 12:34
------------------------------------
@ModifyTime     :  
"""
str = 'Line1-abcdef \nLine2-abc \nLine4-abcd'
print(str.split())
print(str.split(' ',1))
print('-------------------')
s = 'apple,peach,banana,pear'
print(s.split(',',2))
print('-------------------')
s2 = 'asdt\t as \n sada  saa\nasda'
print(s2.split('s'))
print(s2.split('\n'))
'''
['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
['Line1-abcdef', '\nLine2-abc \nLine4-abcd']
-------------------
['apple', 'peach', 'banana,pear']
-------------------
['a', 'dt\t a', ' \n ', 'ada  ', 'aa\na', 'da']
['asdt\t as ', ' sada  saa', 'asda']
'''