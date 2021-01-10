# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  capitaliterator.py
@Description    :  
@CreateTime     :  2021-1-10 17:58
------------------------------------
@ModifyTime     :  
"""
class CapitalIterator:
    def __init__(self,s):
        self.words = [w.title() for w in s.split()]
        self.index = 0

    def __next__(self):
        if self.index == len(self.words):
            raise StopIteration()
        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        return self

class CapitalIterable:
    def __init__(self,s):
        self.s = s

    def __iter__(self):
        return CapitalIterator(self.s)

# iterable then iterator
iterable = CapitalIterable('the brightest star in the night sky')
# get an iterator using iter()
# the argument must supply its own iterator
iterator = iter(iterable) # cal __iter__

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

print('1-----------------')
for w in iterable:
    print(w)
print('2----------------')
for w in iterable:
    print(w)
print('3-----------------')
iterator = iter(iterable)
for w in iterator:
    print(w)
print('4-----------------')
# iterator has been exausted
for w in iterator:
    print(w)
print('5-----------------')
'''
The
Brightest
Star
In
The
Night
Sky
1-----------------
The
Brightest
Star
In
The
Night
Sky
2----------------
The
Brightest
Star
In
The
Night
Sky
3-----------------
The
Brightest
Star
In
The
Night
Sky
4-----------------
5-----------------
'''