# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  testbreak.py
@Description    :  
@CreateTime     :  2021-1-15 14:56
------------------------------------
@ModifyTime     :  
"""
for i in range(1,4):
    for j in range(1,4):
        if i * j > 2:
            break
        print('i * j',i * j)
    print('i is ',i)
'''
i * j 1
i * j 2
i is  1
i * j 2
i is  2
i is  3
'''