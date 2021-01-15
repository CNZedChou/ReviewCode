# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  TestBooleanOperators.py
@Description    :  
@CreateTime     :  2021-1-15 13:44
------------------------------------
@ModifyTime     :  
"""
number = eval(input('Enter a integer:'))
if number % 2 == 0 and number % 3 == 0:
    print(number ,'is divisible by 2 and 3')
if number % 2 == 0 or number % 3 ==0:
    print(number,'is divisible by 2 or 3')
if (number % 2 == 0 or number % 3 == 0) and not (number % 2 == 0 and number % 3 == 0):
    print(number,'is divisible by 2 or 3 but not both')
'''
Enter a integer:18
18 is divisible by 2 and 3
18 is divisible by 2 or 3
Enter a integer:15
15 is divisible by 2 or 3
15 is divisible by 2 or 3 but not both
'''