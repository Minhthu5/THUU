# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 23:53:19 2024

@author: phamnguyenthiminhthu
"""
day = int(input("Nhập ngày (ví dụ 05): "))
month = int(input("Nhập tháng (ví dụ 02): "))
year = int(input("Nhập năm (ví dụ 2005): "))
print("a) Ngày/tháng/năm: {}/{}/{}".format(day, month, year))
short_year = year % 100
print("b) Ngày/tháng/năm (năm 2 chữ số): {}/{}/{}".format(day, month, short_year))
print("c) Năm/tháng/ngày: {}/{}/{}".format(year, month, day))

