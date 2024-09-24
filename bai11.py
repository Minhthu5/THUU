# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:32:33 2024

@author: phamnguyenthiminhthu
"""

chu_thuong = input("Nhập ký tự chữ thường: ")
if len(chu_thuong) == 1 and chu_thuong.islower():
    chu_hoa = chu_thuong.upper()
print("Ký tự chữ hoa tương ứng là:", chu_hoa)
