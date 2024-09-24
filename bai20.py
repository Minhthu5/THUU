# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:49:28 2024

@author: phamnguyenthiminhthu
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
lon_nhat = a
if b > lon_nhat:
    lon_nhat = b
if c > lon_nhat:
    lon_nhat = c
print("Số lớn nhất là:", lon_nhat)
        