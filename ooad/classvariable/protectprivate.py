# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  protectprivate.py
@Description    :  
@CreateTime     :  2021-1-10 16:17
------------------------------------
@ModifyTime     :  
"""
class Wallet:
    def __init__(self,rmb = 0,cad = 0,gbp = 0):
        self.rmb = rmb
        self._cad = cad
        self.__gbp = gbp

    def deposit(self,amount,currency):
        if currency.lower() == 'rmb':
            self.rmb += amount
        if currency.lower() == 'cad':
            self._cad += amount
        if currency.lower() == 'gbp':
            self.__gbp += amount

    def withdraw(self,amount,currency):
        if currency.lower() == 'rmb':
            self.rmb -= amount
        if currency.lower() == 'cad':
            self._cad -= amount
        if currency.lower() == 'gbp':
            self.__gbp -= amount

    def check(self):
        s = ''
        if self.rmb > 0:
            s += '%.0f RMB' % self.rmb
        if self._cad > 0:
            s += '%.0f CAD' % self._cad
        if self.__gbp > 0:
            s += '%.0f GBP' % self.__gbp

if __name__ == '__main__':
    w = Wallet()
    print(w.rmb)
    print(w._cad)
    # print(w.__gbp)
    print(w)
    print(Wallet)
    print(Wallet.__dict__)
    print(w.__dict__)
'''
0
0
Traceback (most recent call last):
  File "F:/GitRepository/ReviewCode/ooad/protectprivate.py", line 48, in <importmodule>
    print(w.__gbp)
AttributeError: 'Wallet' object has no attribute '__gbp'
<__main__.Wallet object at 0x0000020C3BE40668>
<class '__main__.Wallet'>
{'deposit': <function Wallet.deposit at 0x0000020C3BE53488>, 'withdraw': <function Wallet.withdraw at 0x0000020C3BE53510>, '__weakref__': <attribute '__weakref__' of 'Wallet' objects>, '__doc__': None, '__dict__': <attribute '__dict__' of 'Wallet' objects>, '__module__': '__main__', '__init__': <function Wallet.__init__ at 0x0000020C3BE53400>, 'check': <function Wallet.check at 0x0000020C3BE53598>}
{'_Wallet__gbp': 0, 'rmb': 0, '_cad': 0}
'''