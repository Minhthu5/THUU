# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:31:51 2024

@author:phamnguyenthiminhthu
"""

def gio_phut_giay_sang_giay(gio, phut, giay):
  "Chuyển đổi thời gian từ giờ, phút, giây sang giây"
  tong_giay = gio * 3600 + phut * 60 + giay
  return tong_giay
gio = int(input("Nhập số giờ: "))
phut = int(input("Nhập số phút: "))
giay = int(input("Nhập số giây: "))
ket_qua = gio_phut_giay_sang_giay(gio, phut, giay)
print(f"{gio} giờ {phut} phút {giay} giây = {ket_qua} giây")