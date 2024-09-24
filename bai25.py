# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 23:40:28 2024

@author: Pham Nguyen Thi Minh Thu
"""
chu_cai = input("Nhập một chữ cái: ")
if chu_cai.islower():
    chu_cai_moi = chu_cai.upper()
else: 
    chu_cai_moi = chu_cai.lower()
print(f"Chữ cái sau khi chuyển đổi là: {chu_cai_moi}")
