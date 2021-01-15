# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  stripmethod.py
@Description    :  
@CreateTime     :  2021-1-15 11:30
------------------------------------
@ModifyTime     :  
"""
s = '\t Welcome \n'
print(s)
print('-----------------')
s1 = s.strip()
print(s1)
print('-----------------')
s2 = ' \tGood\tMorning\n'
print(s2)
print('-----------------')
s3 = s2.strip()
print(s3)
'''
	 Welcome 

-----------------
Welcome
-----------------
 	Good	Morning

-----------------
Good	Morning
'''