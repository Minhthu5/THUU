# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:38:41 2024

@author: phamnguyenthiminhthu
"""
N = int(input("Nhập vào số nguyên dương N: "))
if N <= 1:
    print(f"{N} không phải là số nguyên tố.")
else:
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            print(f"{N} không phải là số nguyên tố.")
            break
    else:
        print(f"{N} là số nguyên tố.")