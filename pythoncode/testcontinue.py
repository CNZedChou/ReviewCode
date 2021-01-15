# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  testcontinue.py
@Description    :  
@CreateTime     :  2021-1-15 14:58
------------------------------------
@ModifyTime     :  
"""
for i in range(1,4):
    for j in range(1,4):
        if i * j > 2:
            continue
        print('i * j ',i * j)

    print(i)

'''
i * j  1
i * j  2
1
i * j  2
2
3
'''