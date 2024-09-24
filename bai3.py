# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:05:27 2024

@author:  Phạm Nguyễn Thị Minh Thư
"""
a = int(input("Nhập số nguyên dương a: "))
b = int(input("Nhập số nguyên dương b: "))
if a <= 0 or b <= 0:
    print("Cả hai số đều phải là số nguyên dương.")
else:
    phan_nguyen = a // b
    phan_du = a % b
print("Kết quả chia lấy phần nguyên của {} với {} là: {}".format(a, b, phan_nguyen))
print("Kết quả chia lấy phần dư của {} với {} là: {}".format(a, b, phan_du))
