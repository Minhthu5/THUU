# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 18:27:41 2024

@author: phamnguyenthiminhthu
"""
can_nang = float(input("nhap can nang cua ban(kg): "))
chieu_cao = float(input("nhap chieu cao cua ban(m): "))
bmi = can_nang / (chieu_cao * chieu_cao)
bmi_lam_tron = round(bmi, 2)
print("Chỉ số BMI của bạn là: ",bmi_lam_tron)
if bmi < 18.5:
    print("Bạn đang bị thiếu cân.")
elif 18.5 <= bmi < 24.9:
    print("Bạn có cân nặng bình thường.")
elif 25 <= bmi < 29.9:
    print("Bạn đang bị thừa cân.")
else:
    print("Bạn đang bị béo phì.")