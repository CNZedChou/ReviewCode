# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  nestedloop3.py
@Description    :  
@CreateTime     :  2021-1-15 14:41
------------------------------------
@ModifyTime     :  
"""
for i in range(1,9):
    for j in range(9 - 1 - i,0, -1):
        print(' '*4,end='')
    for j in range(0,i):
        print(format(2**j,'>4d'),end='')
    if i > 1:
        for j in range(i-1,0,-1):
            print(format(2**(j-1),'>4d'),end='')
    print()

'''
                               1
                           1   2   1
                       1   2   4   2   1
                   1   2   4   8   4   2   1
               1   2   4   8  16   8   4   2   1
           1   2   4   8  16  32  16   8   4   2   1
       1   2   4   8  16  32  64  32  16   8   4   2   1
   1   2   4   8  16  32  64 128  64  32  16   8   4   2   1
'''