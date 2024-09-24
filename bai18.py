# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:42:50 2024

@author: Phạm Nguyễn Thị Minh Thư
"""
print("PT giờ")
h = int(input("nhập số giờ thứ nhất: "))
m = int(input("nhập số phút thứ nhất: "))
s = int(input("Nhập số giây thứ nhất: "))
hh = int(input("nhập số giờ thứ hai: "))
mm = int(input("nhập số phút thứ hai: "))
ss = int(input("Nhập số giây thứ hai: "))
H = h + hh
M = m + mm
S = s + ss
H1 = h - hh
M1 = m - mm
S1 = s - ss
print("Kết quả cộng là: ",H,"h",M,"m",S,"s")
print("Kết quả trừ là: ",H1,"h",M1,"m",S1,"s")
