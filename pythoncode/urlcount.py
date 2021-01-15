# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  urlcount.py
@Description    :  
@CreateTime     :  2021-1-15 16:15
------------------------------------
@ModifyTime     :  
"""
import urllib.request
def main():
    url = input('URL:').strip()
    infile = urllib.request.urlopen(url)
    s = infile.read().decode()
    counts = countLetters(s.lower())
    for i in range(len(counts)):
        if counts[i] != 0:
            print(chr(ord('a') + i) + " appears " + str(counts[i]) + (' time' if counts[i] == 1 else 'times'))


def countLetters(s):
    counts = 26 * [0]
    for ch in s:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1

    return counts
main()