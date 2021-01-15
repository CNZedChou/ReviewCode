# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  BinaryIODemo.py
@Description    :  
@CreateTime     :  2021-1-15 16:38
------------------------------------
@ModifyTime     :  
"""
import pickle
def main():
    outfile = open("pickle.dat","wb")
    pickle.dump(45,outfile)
    pickle.dump(56.6,outfile)
    pickle.dump('Programming is fun',outfile)
    pickle.dump([1,2,3,4],outfile)
    outfile.close()
    infile = open("pickle.dat","rb")
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))
    infile.close()
main()

