# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  innerclass.py
@Description    :  
@CreateTime     :  2021-1-10 16:05
------------------------------------
@ModifyTime     :  
"""
def format_string(s,formatter = None):
    # an inner class
    class DefaultFormatter:
        def format(self,s):
            return str(s).title()

    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(s)

def format_string2(s):
    # an inner function
    def helper(w):
        return w[0].upper() + w[1:]
    result = ''

    for w in s.split():
        result += helper(w) + ' '
    return result.strip()

if __name__ == '__main__':
    print(format_string('HELLO WORLD'))
    print('------------------------')
    print(format_string2('hello world'))

'''
Hello World
------------------------
Hello World
'''