# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  objectsinteract.py
@Description    :  
@CreateTime     :  2021-1-10 00:07
------------------------------------
@ModifyTime     :  
"""
class Orange:
    '''A blueprint for making many oranges'''

    def __init__(self, weight, orchard, date_picked):
        self.weight = weight
        self.orchard = orchard
        self.date = date_picked

    def pick(self,basket):
        basket.accept(self)

    def __str__(self):
        return 'Orange Info: %.2f libs picked on %s from %s ' % (self.weight, self.date, self.orchard)

    def squeeze(self):
        juice = self.weight * 0.7
        self.weight = self.weight - juice
        return juice

class Basket:
    def __init__(self,location):
        self.location = location
        self.oranges = []

    def accept(self,item):
        self.oranges.append(item)

    def sell(self,customer):
        while self.oranges:
            o = self.oranges.pop()
            customer.purchase(o)
    def discard(self):
        self.oranges = []

class Customer:
    def __init__(self,name):
        self.name = name
        self.purchase_history = ''

    def purchase(self,item):
        self.purchase_history += str(item) + '\n'

    def get_purchase_history(self):
        return '%s has purchased :\n' % self.name + self.purchase_history

basket = Basket('Margate')
orange1 = Orange(0.5,'Sutton','2018-09-16')
orange2 = Orange(0.4,'Holloway','2018-09-16')
orange3 = Orange(0.3,'Oldham','2018-09-16')
orange3.squeeze()
customer1 = Customer('Pooter')
customer2 = Customer('Lupin')
orange1.pick(basket)
orange2.pick(basket)
orange3.pick(basket)

basket.sell(customer1)
basket.sell(customer2)

print(customer1.get_purchase_history())
print(customer2.get_purchase_history())

'''
Pooter has purchased :
Orange Info: 0.09 libs picked on 2018-09-16 from Oldham 
Orange Info: 0.40 libs picked on 2018-09-16 from Holloway 
Orange Info: 0.50 libs picked on 2018-09-16 from Sutton 

Lupin has purchased :


'''