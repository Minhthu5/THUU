# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:30:59 2024

@author: phamnguyenthiminhthu
"""
km = float(input("Nhập vào số km đi được: "))
gia_cuoc = 0
if km <= 1:
    gia_cuoc = 15000
elif km <= 5:
    gia_cuoc = 15000 + (km - 1) * 13500
else:
    gia_cuoc = 15000 + 4 * 13500 + (km - 5) * 11000
if km > 120:
    gia_cuoc *= 0.9
print(f"Tổng tiền cước taxi là: {gia_cuoc:.0f}đ")
