# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  formatting.py
@Description    :  
@CreateTime     :  2021-1-15 12:26
------------------------------------
@ModifyTime     :  
"""
amount = 12618.98
interestRate = 0.0013
interest = amount * interestRate
print('Interest is ',interest)
print('Interest is ',round(interest,2))
print('Interest is ',format(interest,'.2f'))
