# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  yield.py
@Description    :  
@CreateTime     :  2021-1-10 19:45
------------------------------------
@ModifyTime     :  
"""
def foo():
    print('BEGIN')
    for i in range(3):
        print('before yield %d.'%i)
        yield i
        print('after yield %d'%i)
    print('END')

gen = foo()
x = next(gen)
y = next(gen)
z = next(gen)
# a = next(gen)
'''
BEGIN
before yield 0.
after yield 0
before yield 1.
after yield 1
before yield 2.
END
Traceback (most recent call last):
File "F:/GitRepository/ReviewCode/ooad/designpattern/iterator/generators/yield.py", line 25, in <module>
    a = next(gen)
StopIteration
'''