# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  scoreproperty.py
@Description    :  
@CreateTime     :  2021-1-9 23:13
------------------------------------
@ModifyTime     :  
"""
class Score0:
    def __init__(self,value,date):
        self.value = value
        self.date = date

class Score:
    def __init__(self,value,date):
        self._score = value
        self._score = date

    @property
    def value(self):
        return self._score

    @value.setter
    def value(self,v):
        if v > 100 or v < 0:
            raise Exception('Score value out of range')
        self._score = v

class Score2:
    def __init__(self,value,date):
        self._score = value
        self._date = date

    def getter(self):
        return self._score


    def setter(self,v):
        if v > 100 or v < 0:
            raise Exception('Score value out of range')
        self._score = v

    value = property(fget=getter,fset=setter)


if __name__ == '__main__':
    s0 = Score0(60,'20191216')
    print(s0.value)
    s0.value = 101
    print(s0.value)

    s = Score(60,'20191216')
    # s.value = 101


    s2 = Score2(60,'20191216')
    s2.value = -1
    print(s2.value)

'''
60
101
Traceback (most recent call last):
  File "F:/GitRepository/ReviewCode/ooad/scoreproperty.py", line 54, in <module>
    s.value = 101
  File "F:/GitRepository/ReviewCode/ooad/scoreproperty.py", line 30, in value
    raise Exception('Score value out of range')
Exception: Score value out of range
Traceback (most recent call last):
  File "F:/GitRepository/ReviewCode/ooad/scoreproperty.py", line 61, in <module>
    s2.value = -1
  File "F:/GitRepository/ReviewCode/ooad/scoreproperty.py", line 44, in setter
    raise Exception('Score value out of range')
Exception: Score value out of range
'''