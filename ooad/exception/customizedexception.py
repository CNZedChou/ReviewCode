# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  customizedexception.py
@Description    :  
@CreateTime     :  2021-1-10 17:39
------------------------------------
@ModifyTime     :  
"""
class InvalidWithdrawal(Exception):
    def __init__(self,balance,amount):
        super().__init__('account dose not have ${}'.format(amount))
        self.amount = amount
        self.balance = balance

    def overdraft(self):
        return self.amount - self.balance


if __name__ == '__main__':

    try:
        raise InvalidWithdrawal(25,50)
    except InvalidWithdrawal as e:
        print('Overdraft ${}'.format(e.overdraft()))
'''
Overdraft $25
'''