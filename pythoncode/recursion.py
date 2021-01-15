# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  recursion.py
@Description    :  
@CreateTime     :  2021-1-15 16:55
------------------------------------
@ModifyTime     :  
"""
def f(n):
    if n > 0:
        print(n % 10)
    f(n // 10)
def main():
    f(123456)
main()