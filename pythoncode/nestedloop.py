# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  nestedloop.py
@Description    :  
@CreateTime     :  2021-1-15 14:35
------------------------------------
@ModifyTime     :  
"""
for i in range(1,5):
    j = 0
    while j < i:
        print(j,end=' ')
        j += 1

'''
0 0 1 0 1 2 0 1 2 3 
'''