# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:24:23 2024

@author: phamnguyenthiminhthu
"""
month = int(input("Nhập tháng (1-12): "))
year = int(input("Nhập năm: "))
nam_nhuan = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if month in [1, 3, 5, 7, 8, 10, 12]:
    print(f"Tháng {month} có 31 ngày.")
elif month in [4, 6, 9, 11]:
    print(f"Tháng {month} có 30 ngày.")
elif month == 2:
    print(f"Tháng 2 có {29 if nam_nhuan else 28} ngày.")
else:
    print("Tháng không hợp lệ!")
