# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  superfunc.py
@Description    :  
@CreateTime     :  2021-1-10 13:02
------------------------------------
@ModifyTime     :  
"""
class Contact:
    all_contacts = []

    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

    def __str__(self):
        return '%s <%s>'%(self.name,self.email)

class Friend(Contact):
    def __init__(self,name,email,phone):
        # print(id(super()))
        super().__init__(name,email)
        self.phone = phone

    def __str__(self):
        return super().__str__() + ' phone:%s'%self.phone

class Supplier(Contact):
    def order(self,order):
        print('Send %s to %s' % (order.upper(),self.name))

f1 = Friend('Bob','bob@wonderland.com','(010) 8793180')
f2 = Friend('Nick','nick@starbucks.com','(0579) 2865 2288')
print('---------------')
print(f1)
print(f2)
print('---------------')
print(id(f1))
print(id(f2))
print('---------------')
print(id(f1.all_contacts))
print(id(f2.all_contacts))
print(id(Friend.all_contacts))
print('----------------')
s = Supplier('Pizza Hut','order@pizzahut.com')
s.order('8 Chicken wings')
print(id(s.all_contacts))
for p in s.all_contacts:
    print(p)
'''
---------------
Bob <bob@wonderland.com> phone:(010) 8793180
Nick <nick@starbucks.com> phone:(0579) 2865 2288
---------------
3128763706336
3128763706392
---------------
3128813242056
3128813242056
3128813242056
----------------
Send 8 CHICKEN WINGS to Pizza Hut
3128813242056
Bob <bob@wonderland.com> phone:(010) 8793180
Nick <nick@starbucks.com> phone:(0579) 2865 2288
Pizza Hut <order@pizzahut.com>
'''