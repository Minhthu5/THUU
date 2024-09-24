# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:54:21 2024

@author: phamnguyenthiminhthu
"""
def tinh_tong(N):
  tong = 0
  for i in range(N+1):
    mau = 2*i + 1
    tong += 1 / mau
  return tong
N = int(input("Nhập số lượng số hạng N: "))
ket_qua = tinh_tong(N)
print("Tổng của dãy số là:", ket_qua)
