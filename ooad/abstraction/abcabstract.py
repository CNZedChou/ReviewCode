# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  abcabstract.py
@Description    :  
@CreateTime     :  2021-1-10 16:26
------------------------------------
@ModifyTime     :  
"""
from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def speak(self):
        print('Un-gu')

    @abstractmethod
    def add(self,a,b):
        pass

class S(A):
    def speak(self):
        super().speak()
        print('Every Sha-la-la Every Wo-o-wo-o')

    def add(self,x,y):
        return x + y

a = S()
a.speak()
'''
Un-gu
Every Sha-la-la Every Wo-o-wo-o
'''