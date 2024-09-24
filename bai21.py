# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 19:18:11 2024

@author: Phạm Nguyễn Thị Minh Thư
"""
so = int(input("Nhập một số bất kỳ: "))
x = {0:"không", 1:"một", 2:"hai", 3:"ba", 4:"bốn", 5:"năm", 6:"sáu", 7:"bảy", 8:"tám", 9:"chín"}
if 0 <= so <= 9:
    print("Giá trị của số là: ",(x[so]))
else:
    print("Không đọc được số.")