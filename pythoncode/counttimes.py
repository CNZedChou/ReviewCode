# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  counttimes.py
@Description    :  
@CreateTime     :  2021-1-15 15:41
------------------------------------
@ModifyTime     :  
"""
class Count:
    def __init__(self,count = 0):
        self.count = count

def main():
    c = Count()
    times = 0
    for i in range(100):
        increment(c,times)
    print('count is',c.count)
    print('time is ',times)

def increment(c,times):
    # c = Count(times)
    c.count += 1
    times += 1

main()
'''
count is 0
time is  0
'''