# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  coroutine2.py
@Description    :  
@CreateTime     :  2021-1-10 21:01
------------------------------------
@ModifyTime     :  
"""
def echo():
    just_received = 'nothing'
    try:
        while True:
            received = yield just_received
            just_received = received
            print('i god {}'.format(just_received))
    except GeneratorExit:
        print('Coroutine closed')

