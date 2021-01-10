# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  decorator3.py
@Description    :  
@CreateTime     :  2021-1-10 22:18
------------------------------------
@ModifyTime     :  
"""
import time
def log_calls(func):
    def wrapper(*args,**kwargs):
        now = time.time()
        print('DECOR Calling {0} with {1} and {2}'.format(func.__name__,args,kwargs))
        return_val = func(*args,**kwargs)
        print('DECOR Finished {0} in {1}ms\n'.format(func.__name__,time.time() - now))
        return return_val
    return wrapper


def test1(a,b,c):
    print('test1 called')

def test2(a,b):
    print('test2 called')

def test3(a,b):
    print('test3 called')
    time.sleep(1)

@log_calls
def test4(a,b):
    print('test4 called')

test1 = log_calls(test1)
test2 = log_calls(test2)
test3 = log_calls(test3)

test1(1,2,3)
test2(4,b = 5)
test3(6,7)
test4(8,9)
