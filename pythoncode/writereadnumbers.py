# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  writereadnumbers.py
@Description    :  
@CreateTime     :  2021-1-15 16:05
------------------------------------
@ModifyTime     :  
"""
from random import randint
def main():
    outfile = open('Numbers.txt','w')
    for i in range(10):
        outfile.write(str(randint(0,9))+' ')
    outfile.close()
    infile = open('Numbers.txt','r')
    s = infile.read()
    numbers = [eval(x) for x in s.split()]
    for number in numbers:
        print(number,end=' ')
    infile.close()

main()
'''
8 2 7 8 6 0 6 5 7 0 
'''