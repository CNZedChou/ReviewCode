# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  Lottery.py
@Description    :  
@CreateTime     :  2021-1-15 13:50
------------------------------------
@ModifyTime     :  
"""
import random
lottery = random.randint(10,99)
guess = eval(input('Enter your number'))
print('lottery is',lottery)
lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery // 10
guessDigit1 = guess // 10
guessDigit2 = guess % 10
if lottery == guess:
    print('Perfect match, $10')
elif lotteryDigit1 == guessDigit2 and lotteryDigit2 ==guessDigit1:
    print('all match $3')
elif lotteryDigit1 == guessDigit2 or lotteryDigit1 == guessDigit1 or lotteryDigit2 == guessDigit1 or lotteryDigit2 == guessDigit1:
    print('one match $1')
else:
    print('no match')
