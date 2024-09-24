# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:56:02 2024

@author: phamnguyenthiminhthu
"""
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")
else:
    x = -b / a
    print(f"Nghiệm của phương trình {a}x + {b} = 0 là: x = {x}")
