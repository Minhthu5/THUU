# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:13:08 2024

@author: phamnguyenthiminhthu
"""
a = int(input("nhập số đầu tiên: "))
b = int(input("nhập số thứ hai: "))
c = int(input("nhập số thứ ba: "))
d = int(input("nhập số thứ tư: "))
sonut = a + b + c + d
if sonut%10 == 0:
    print("Số nút là 0")
else:
    print("Số nút là ",sonut%10)


