# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 11:29:54 2024

@author: phamnguyenthiminhthu
"""

print("============ MENU ============")
print("1. Hu tieu")
print("2. Chao long")
print("3. Banh canh")
print("4. Bun rieu")
print("5. Pho bo")
print("==============================")
lua_chon = input("Mời nhập lựa chọn (1-5): ")
print("==============================")
if lua_chon == '1':
    print("Bạn đã chọn Hu tieu.")
elif lua_chon == '2':
    print("Bạn đã chọn Chao long.")
elif lua_chon == '3':
    print("Bạn đã chọn Banh canh.")
elif lua_chon == '4':
    print("Bạn đã chọn Bun rieu.")
elif lua_chon == '5':
    print("Bạn đã chọn Pho bo.")
else:
    print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 5.")