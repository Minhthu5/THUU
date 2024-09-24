# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:53:32 2024

@author: phamnguyenthiminhthu
"""

a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print(f"Ba số theo thứ tự tăng dần là: {a}, {b}, {c}")
N = input("Nhập vào 1 số nguyên N: ")
sap_xep = "".join(sorted(N))
print(f"Thứ tự tăng dần của dãy số là: {sap_xep}")
