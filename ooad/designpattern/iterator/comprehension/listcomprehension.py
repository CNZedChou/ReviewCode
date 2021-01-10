# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  listcomprehension.py
@Description    :  
@CreateTime     :  2021-1-10 18:12
------------------------------------
@ModifyTime     :  
"""
slst = ['1','12','123','1234']
int_lst = [int(s) for s in slst if len(s) > 2]
