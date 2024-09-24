# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:14:41 2024

@author: Phạm Nguyễn Thị Minh Thư
"""

gio = int(input("Nhập giờ (0-23): "))
phut = int(input("Nhập phút (0-59): "))
giay = int(input("Nhập giây (0-59): "))
if 0 <= gio <= 23 and 0 <= phut <= 59 and 0 <= giay <= 59:
    print("Tổng số giây là {}:{}:{}".format(gio, phut, giay))
else:
    print("Giá trị nhập vào không hợp lệ. Hãy kiểm tra lại giờ, phút và giây.")