# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  nestedloop2.py
@Description    :  
@CreateTime     :  2021-1-15 14:39
------------------------------------
@ModifyTime     :  
"""
i = 5
while i >= 1:
    num = 1
    for j in range(1,i + 1):
        print(num,end='xxx')
        num *= 2

    print()
    i -= 1
'''
1xxx2xxx4xxx8xxx16xxx
1xxx2xxx4xxx8xxx
1xxx2xxx4xxx
1xxx2xxx
1xxx
'''