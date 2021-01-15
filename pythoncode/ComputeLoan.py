# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  ComputeLoan.py
@Description    :  
@CreateTime     :  2021-1-15 11:10
------------------------------------
@ModifyTime     :  
"""
annualInterestRate = eval(input('Enter annual interest rate'))
monthlyInterestRate = annualInterestRate / 1200
numberOfYears = eval(input('Enter the number of the years'))
loanAmount = eval(input('Enter loan amount'))
monthlyPayment = loanAmount * monthlyInterestRate / (1 - 1/(1 + monthlyInterestRate)**(numberOfYears * 12))
totalPayment = monthlyPayment * numberOfYears *12

print('The monthly payment is ',int(monthlyPayment))
print('Total payment is ',int(totalPayment))