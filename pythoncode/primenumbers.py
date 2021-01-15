# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  primenumbers.py
@Description    :  
@CreateTime     :  2021-1-15 15:03
------------------------------------
@ModifyTime     :  
"""
import math
NUMBER_OF_PRIMES = 50
PRIMES_PER_LINE = 10
count = 0
number = 2
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

while count < NUMBER_OF_PRIMES:
    if isPrime(number):
        count += 1
        print(format(number,'5d'),end=' ')
        if count % PRIMES_PER_LINE == 0:
            print()
    number += 1
