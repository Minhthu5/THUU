# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:44:19 2024

@author: phamnguyenthiminhthu
"""
n = int(input("Nhập vào số nguyên dương chẵn n: "))
if n > 0 and n % 2 == 0:
    S = sum(i for i in range(2, n + 1, 2))
    print(f"Tổng S từ 2 đến {n} là: {S}")
else:
    print("Số nhập vào phải là số chẵn và lớn hơn 0.")
