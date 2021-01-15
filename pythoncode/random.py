# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  random.py
@Description    :  
@CreateTime     :  2021-1-15 13:29
------------------------------------
@ModifyTime     :  
"""
import random
rand1 = random.randrange(1,7,4)
rand2 = random.randrange(1,7,4)
print(rand1)
print(rand2)
rand3 = random.sample(range(1,100),3)
print(rand3)
'''
5
1
[34, 69, 77]
'''