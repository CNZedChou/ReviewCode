# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  DetectEndOfFile.py
@Description    :  
@CreateTime     :  2021-1-15 16:41
------------------------------------
@ModifyTime     :  
"""
import pickle
def main():
    outfile = open('numbers.dat','wb')
    data = eval(input('Enter an integer(end with 0'))
    while data != 0:
        pickle.dump(data,outfile)
        data = eval(input('Enter an integer(end with 0'))
    outfile.close()
    infile = open('numbers.dat','rb')
    end_of_file = False
    while not end_of_file:
        try:
            print(pickle.load(infile),end=' ')
        except EOFError:
            end_of_file = True

    infile.close()
    print('\n all read')
main()