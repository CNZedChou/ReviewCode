# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  coroutine3.py
@Description    :  
@CreateTime     :  2021-1-10 21:05
------------------------------------
@ModifyTime     :  
"""
def tally():
    score = 0
    while True:
        incr = yield score
        score += incr

bluejays = tally()
next(bluejays)
print(bluejays.send(1))
print(bluejays.send(2))

whitesox = tally()
next(whitesox)
print(whitesox.send(2))
print(whitesox.send(1))