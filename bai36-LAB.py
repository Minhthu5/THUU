# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:42:51 2024

@author: phamnguyenthiminhthu
"""
N = int(input("Nhập vào số nguyên dương N: "))
if N > 0:
    S = sum(i**2 for i in range(1, N + 1))
    print(f"Tổng S từ 1^2 đến {N}^2 là: {S}")
else:
    print("Số nhập vào không phải là số nguyên dương.")
