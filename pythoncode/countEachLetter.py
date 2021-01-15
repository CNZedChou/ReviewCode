
# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  countEachLetter.py
@Description    :  
@CreateTime     :  2021-1-15 16:09
------------------------------------
@ModifyTime     :  
"""
def main():
    filename = input('Filename:').strip()
    infile = open(filename,'r')
    counts = [0] *26
    for line in infile:
        countLetters(line.lower(),counts)
    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a')+i)+" appears "+str(counts[i])+(' time' if counts[i] == 1 else 'times'))


def countLetters(line,counts):
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1

main()