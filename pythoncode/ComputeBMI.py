# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@Author         :  Zed
@Version        :  V1.0.0
------------------------------------
@File           :  ComputeBMI.py
@Description    :  
@CreateTime     :  2021-1-15 13:35
------------------------------------
@ModifyTime     :  
"""
weight = eval(input('Enter weight in pounds'))
height = eval(input('Enter height in inches'))
KILOGRAM_PER_POUND = 0.45359237
METERS_PER_INCH = 0.0254
weightInKilograms = weight * KILOGRAM_PER_POUND
heightInMeters = height * METERS_PER_INCH
bmi = weightInKilograms / (heightInMeters * heightInMeters)
print('BMI is ',format(bmi,'.2f'))
if bmi < 18.5:
    print('Underweight')
elif bmi < 25:
    print('Normal')
elif bmi < 30:
    print('Overweight')
else:
    print('Obese')

'''
Enter weight in pounds146
Enter height in inches70
BMI is  20.95
Normal
'''
