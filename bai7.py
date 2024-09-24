# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:11:25 2024

@author: phamnguyenthiminhthu
"""
import math
ban_kinh = float(input("nhap ban kinh hinh tron: "))
chu_vi = 2 * math.pi * ban_kinh
dien_tich = math.pi * ban_kinh ** 2 
cv = round(chu_vi, 2)
dt = round(dien_tich, 2)
print(f"Chu vi của hình tròn là: ", cv)
print(f"Diện tích của hình tròn là: ", dt)

