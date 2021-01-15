# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  multisubstraction.py
@Description    :  
@CreateTime     :  2021-1-15 14:23
------------------------------------
@ModifyTime     :  
"""
import random
import time

correctCount = 0
count = 0
NUMBER_OF_QUESTION = 5

startTime =time.time()

while count <NUMBER_OF_QUESTION:
    number1 = random.randint(0,9)
    number2 = random.randint(0,9)

    if number1 < number2:
        number1,number2 = number2,number1

    answer = eval(input('Answer to '+str(number1)+'-'+str(number2)))
    if number1 - number2 == answer:
        print('Correct')
        correctCount += 1
    else:
        print('Wrong,Correct answer is ',str(number1 - number2))

    count += 1

endTime = time.time()
print('Correct count is',correctCount,'time is ',int(endTime - startTime))
