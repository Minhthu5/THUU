# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:58:22 2024

@author:  phamnguyenthiminhthu
"""
import math
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
print(f"{a}x^2 + {b}x + {c} = 0")
delta = b**2 - 4*a*c
if delta > 0:
 x1 = (-b + math.sqrt(delta)) / (2 * a)
 x2 = (-b - math.sqrt(delta)) / (2 * a)
 print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1} và x2 = {x2}")
elif delta == 0:
 x = -b / (2 * a)
 print(f"Phương trình có một nghiệm kép: x = {x}")
else:
 print("Phương trình vô nghiệm.")