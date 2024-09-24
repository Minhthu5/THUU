# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:23:25 2024

@author: PHAMNGUYENTHIMINHTHU
"""

N = int(input("Nhập vào một số nguyên dương N: "))
while N <= 0:
    print("N phải là số nguyên dương. Vui lòng nhập lại!")
    N = int(input("Nhập vào một số nguyên dương N: "))
tong = 0
for i in str(N):
    tong += int(i)
print(f"Tổng các chữ số của {N} là: {tong}")