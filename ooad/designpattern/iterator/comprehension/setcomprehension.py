# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  setcomprehension.py
@Description    :  
@CreateTime     :  2021-1-10 18:37
------------------------------------
@ModifyTime     :  
"""
from collections import namedtuple
Book = namedtuple('Book','author title genre')
books = [Book('Pratchett','Thief of Time','fantasy'),
        Book('Pratchett','Nightwatch','fantasy'),
        Book('Le Guin','The Dispossessed','scifi'),
        Book('Le Guin','A Wizard of Earthsea','fantasy'),
         ]
fantasy_authors = {b.author for b in books if b.genre == 'fantasy'}
print(fantasy_authors)
fantasy_titles = {b.title : b for b in books if b.genre == 'fantasy'}
print(fantasy_titles)
'''
{'Le Guin', 'Pratchett'}
{'Thief of Time': Book(author='Pratchett', title='Thief of Time', genre='fantasy'), 'A Wizard of Earthsea': Book(author='Le Guin', title='A Wizard of Earthsea', genre='fantasy'), 'Nightwatch': Book(author='Pratchett', title='Nightwatch', genre='fantasy')}

'''