# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  listfiles.py
@Description    :  
@CreateTime     :  2021-1-10 19:57
------------------------------------
@ModifyTime     :  
"""
class File:
    def __init__(self,name):
        self.name = name

class Dir(File):
    def __init__(self,name):
        super().__init__(name)
        self.children = []

'''
proj
 - run.py
 - templates
  - a.html
  - b.html
  - old
   - a0.html
   - b0.html   
'''

old = Dir('old')
old.children.append(File('a0.html'))
old.children.append(File('b0.html'))

templates = Dir('templates')
templates.children.append(File('a.html'))
templates.children.append(File('b.html'))
templates.children.append(old)

proj = Dir('proj')
proj.children.append(File('run.py'))
proj.children.append(templates)

def walk(d):
    if isinstance(d,Dir):
        yield d.name + '/'
        for f in d.children:
            yield from walk(f)
    else:
        yield d.name

for f in walk(proj):
    print(f)
'''
proj/
run.py
templates/
a.html
b.html
old/
a0.html
b0.html
'''