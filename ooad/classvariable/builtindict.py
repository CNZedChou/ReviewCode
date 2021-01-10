# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  builtindict.py
@Description    :  
@CreateTime     :  2021-1-10 13:43
------------------------------------
@ModifyTime     :  
"""
class ContactList(list):
    def search(self,name):
        matching_contacts = []
        for contact in self:
            if name in contact.name:
                matching_contacts.append(contact)
        return matching_contacts

class Contact:
    all_contacts = ContactList()
    def __init__(self,name):
        self.name = name
        self.all_contacts.append(self)

c1 = Contact('John A')
c2 = Contact('Robert B')
c3 = Contact('John-Robert C')

for x in c1.all_contacts.search('John'):
    print(x.name)