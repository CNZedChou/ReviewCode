# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  DisplayTime.py
@Description    :  
@CreateTime     :  2021-1-15 11:14
------------------------------------
@ModifyTime     :  
"""
import time
currentTime = time.time()
totalSecond = int(currentTime)
currentSecond = totalSecond % 60
totalMinute = totalSecond // 60
currentMinute = totalMinute % 60
totalHour = totalMinute // 60
currentHour = totalHour % 24
currentYear = 1970 + totalHour //24 //365

print('current year is ',currentYear)
print('current time is ',currentHour,' : ',currentMinute,' : ',currentSecond,' GMT')
'''
current year is  2021
current time is  3  :  26  :  57  GMT

'''