# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:47:58 2024

@author: phamnguyenthiminhthu
"""
def tinh_tong(N):
  tong = 0
  for i in range(1, N+1):
    tong += 1 / i
  return tong
N = int(input("Nhập số lượng số hạng N: "))
ket_qua = tinh_tong(N)
print("Tổng của dãy số là:", ket_qua)

