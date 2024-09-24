# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 15:07:15 2024

@author: phamnguyenthiminhthu
"""
import math
a = float(input("nhập a: "))
b = float(input("nhập b: "))
A = ( (a + b)/(math.pow(a, 1/3)+math.pow(b, 1/3)) - math.pow(a*b, 1/3)) / (math.pow(a, 1/3)-math.pow(b, 1/3))**2
print("kết quả là: ",A)

    