# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:47:29 2024

@author: phamnguyenthiminhthu
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))
nho_nhat = a
if b < nho_nhat:
    nho_nhat = b
if c < nho_nhat:
    nho_nhat = c
if d < nho_nhat:
    nho_nhat = d
print("Số nhỏ nhất là:", nho_nhat)