# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  mixin.py
@Description    :  
@CreateTime     :  2021-1-10 15:13
------------------------------------
@ModifyTime     :  
"""
class Contact:
    all_contacts = []

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.all_contacts.append(self)

    def __str__(self):
        return '%s <%s>' % (self.name, self.email)

class MailSender:
    def send_mail(self,message):
        print('Sending mail to %s with the following content:\n%s'%(self.email,message))


class EmailableContact(Contact,MailSender):
    pass

e = EmailableContact('John','jsmith@gitee.com')
e.send_mail('Hello how are you doing')

'''
Sending mail to jsmith@gitee.com with the following content:
Hello how are you doing
'''

