# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:41:04 2024

@author: phamnguyenthiminhthu
"""
N = int(input("Nhập vào số nguyên dương N: "))
if N > 0:
    S = sum(range(1, N + 1))
    print(f"Tổng S từ 1 đến {N} là: {S}")
else:
    print("Số nhập vào không phải là số nguyên dương.")
