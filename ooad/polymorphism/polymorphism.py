# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  polymorphism.py
@Description    :  
@CreateTime     :  2021-1-10 13:55
------------------------------------
@ModifyTime     :  
"""
class AudioFile:
    def __init__(self,filename):
        if not filename.endswith(self.ext):
            raise Exception('Not recognised file format')
        self.filename = filename

class MP3File(AudioFile):
    ext = 'mp3'
    def play(self):
        print('playing {} as mp3'.format(self.filename))

class WavFile(AudioFile):
    ext = 'wav'
    def play(self):
        print('playing {} as wav'.format(self.filename))

# duck-typing
class FlacFile:
    def __init__(self,filename):
        if not filename.endswith('.flac'):
            raise Exception('Invalid file format')
        self.filename = filename

    def play(self):
        print('playing {} as flac'.format(self.filename))

a = MP3File('music.mp3')
a.play()

b = WavFile('music.wav')
b.play()

# c = MP3File('music.wav')
# c.play()

d = FlacFile('music.flac')
d.play()
'''
playing music.mp3 as mp3
playing music.wav as wav
Traceback (most recent call last):
  File "F:/GitRepository/ReviewCode/ooad/polymorphism.py", line 45, in <importmodule>
    c = MP3File('music.wav')
  File "F:/GitRepository/ReviewCode/ooad/polymorphism.py", line 16, in __init__
    raise Exception('Not recognised file format')
Exception: Not recognised file format
playing music.flac as flac
'''