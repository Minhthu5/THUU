# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:45:55 2024

@author: phamnguyenthiminhthu
"""
n = int(input("Nhập vào số nguyên dương lẻ n: "))
if n > 0 and n % 2 != 0:
    S = 1
    for i in range(1, n + 1):
        S *= i
    print(f"Tổng S từ 1 đến {n} là: {S}")
else:
    print("Số nhập vào phải là số lẻ và lớn hơn 0.")