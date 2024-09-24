# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:36:31 2024

@author: 84982
"""

import math
N = int(input("Nhập vào số nguyên dương N: "))
if N > 0:
    can_bac_2 = math.sqrt(N)  
    if can_bac_2 ** 2 == N:
        print(f"{N} là số chính phương.")
    else:
        print(f"{N} không phải là số chính phương.")
else:
    print("Số nhập vào không phải là số nguyên dương.")