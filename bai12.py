# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:34:02 2024

@author: phamnguyenthiminhthu
"""

import random
A = random.randrange(0, 100, 1)
print("vậy kết quả random là: ", A)
B = random.random() * 100
print("vậy kết quả random là: ", B)
C = random.randrange(50, 99, 1)
print("vậy kết quả random là: ", C)
D = random.random() * (99-50) + 50
print("vậy kết quả random là: ",D)
E = random.randrange(-39, 80, 1)
print("vậy kết quả random là: ", E)
F = random.random() * (79 - (-39)) + (-39)
print("vậy kết quả là: ", F)
G = random.randrange(-79, -38, 1)
print("vậy kết quả là:", G)
H = random.random() * (-39+79) + 79
print("vậy kết quả là:", H)


