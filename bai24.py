# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:38:41 2024

@author: Pham Nguyen Thi Minh Thu
"""

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    print(f"Thời gian hợp lệ: {gio:02}:{phut:02}:{giay:02}")
else:
    print("Thời gian không hợp lệ.")