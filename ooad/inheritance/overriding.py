# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  overriding.py
@Description    :  
@CreateTime     :  2021-1-10 12:51
------------------------------------
@ModifyTime     :  
"""
class Piece:
    def __init__(self,color):
        self.color = color

    def move(self):
        raise NotImplementedError('Subclass must implement the abstract method')

class PuppetKing(Piece):
    def __init__(self,color,shape):
        super().__init__(color)
        self.shape = shape

class King(Piece):
    def __init__(self,color,shape):
        super().__init__(color)
        self.shape = shape

    def move(self):
        print('King Move')

class Player:
    def __init__(self,chess_set):
        self.chess_set = chess_set

    def calculate_move(self):
        print('Randomly pick a piece and make a legal move')

class DeepBlue(Player):
    def __init__(self,chess_set):
        Player.__init__(self,chess_set)

    def calculate_move(self):
        print('Judiciously pick a piece and make a smart move')
