# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  duckisinstance.py
@Description    :  
@CreateTime     :  2021-1-10 16:31
------------------------------------
@ModifyTime     :  
"""
from abc import ABC,abstractmethod

class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

    @classmethod
    def __subclasscheck__(cls, subclass):
        if cls is Bird:
            attrs = set(dir(subclass))
            print(attrs)
            print(set(cls.__abstractmethods__))
            if set(cls.__abstractmethods__) <= attrs:
                return True
        return NotImplemented

class Duck(Bird):
    def fly(self):
        print('Duck flying')

class Airplane(Bird):
    def fly(self):
        print('Airplane flying')

class ParkerSolarProbe:
    def fly(self):
        print('Destination is sun')

if __name__ == '__main__':
    duck = Duck()
    airplane = Airplane()
    parker = ParkerSolarProbe()
    print('isinstance(duck,ABC)',isinstance(duck,ABC))
    print('isinstance(duck,Bird)',isinstance(duck,Bird))
    print('isinstance(airplane,ABC)', isinstance(airplane, ABC))
    print('isinstance(airplane,Bird)', isinstance(airplane, Bird))
    print('isinstance(parker,Bird)',isinstance(parker,Bird))
    print('issubclass(ParkerSolarProbe,Bird)',issubclass(ParkerSolarProbe,Bird))
'''
isinstance(duck,ABC) True
{'__delattr__', '__module__', '__reduce__', '__weakref__', '_abc_cache', '__class__', '__subclasscheck__', '__dict__', '__abstractmethods__', '__reduce_ex__', '__str__', '__doc__', '__sizeof__', '__subclasshook__', '_abc_negative_cache_version', '__getattribute__', '__eq__', '__format__', '__ne__', '__new__', '__hash__', '__gt__', '__setattr__', '__le__', 'fly', '__dir__', '__lt__', '__init__', '__ge__', '_abc_registry', '__repr__', '_abc_negative_cache'}
{'fly'}
isinstance(duck,Bird) True
isinstance(airplane,ABC) True
{'__delattr__', '__module__', '__reduce__', '__weakref__', '_abc_cache', '__class__', '__subclasscheck__', '__dict__', '__abstractmethods__', '__reduce_ex__', '__str__', '__doc__', '__sizeof__', '__subclasshook__', '_abc_negative_cache_version', '__getattribute__', '__eq__', '__format__', '__ne__', '__new__', '__hash__', '__gt__', '__setattr__', '__le__', 'fly', '__dir__', '__lt__', '__init__', '__ge__', '_abc_registry', '__repr__', '_abc_negative_cache'}
{'fly'}
isinstance(airplane,Bird) True
{'__delattr__', '__module__', '__reduce__', '__weakref__', '__class__', '__dict__', '__reduce_ex__', '__str__', '__sizeof__', '__doc__', '__subclasshook__', '__getattribute__', '__eq__', '__format__', '__ne__', '__new__', '__hash__', '__gt__', '__setattr__', '__le__', 'fly', '__dir__', '__lt__', '__init__', '__ge__', '__repr__'}
{'fly'}
isinstance(parker,Bird) True
issubclass(ParkerSolarProbe,Bird) False
'''