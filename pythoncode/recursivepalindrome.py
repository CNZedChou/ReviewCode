# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  recursivepalindrome.py
@Description    :  
@CreateTime     :  2021-1-15 16:57
------------------------------------
@ModifyTime     :  
"""
def isPalindrome(s):
    return isPalindromeHelper(s,0,len(s) -1)

def isPalindromeHelper(s,low,high):
    if high <= low:
        return True
    elif s[low] != s[high]:
        return False
    else:
        return isPalindromeHelper(s,low+1,high-1)