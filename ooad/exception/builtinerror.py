# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  builtinerror.py
@Description    :  
@CreateTime     :  2021-1-10 17:20
------------------------------------
@ModifyTime     :  
"""
class EvenOnly(list):
    def append(self,integer):
        if not isinstance(integer,int):
            raise TypeError('Only integer can be added')
        if integer % 2 != 0:
            raise ValueError('Only even numbers can be added')
        super().append(integer)

if __name__ == '__main__':
    L = EvenOnly()
    L.append(2)
    # L.append('2')
    L.append(3)
'''
Traceback (most recent call last):
  File "F:/GitRepository/ReviewCode/ooad/builtinerror.py", line 24, in <importmodule>
    L.append('2')
  File "F:/GitRepository/ReviewCode/ooad/builtinerror.py", line 16, in append
    raise TypeError('Only integer can be added')
TypeError: Only integer can be added
------------------------------------------------------------------------------
Traceback (most recent call last):
  File "F:/GitRepository/ReviewCode/ooad/builtinerror.py", line 25, in <importmodule>
    L.append(3)
  File "F:/GitRepository/ReviewCode/ooad/builtinerror.py", line 18, in append
    raise ValueError('Only even numbers can be added')
ValueError: Only even numbers can be added
'''