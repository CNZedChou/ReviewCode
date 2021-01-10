# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  tryexcept.py
@Description    :  
@CreateTime     :  2021-1-10 17:32
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
    try:
        L.append(2)
        L.append('2')
        L.append(3)
    except TypeError:
        print('Encountered a Type Error')
    except ValueError:
        print('Encountered a Value Error')
'''
Encountered a Type Error
'''

