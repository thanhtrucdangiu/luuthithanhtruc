# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:34:24 2024

@author: Student
"""
x= float(input("Nhap do dai doan duong den truong (m):"))
if x <300:
    print("Duong den truong qua gan. Thoi! di bo")
elif x >1200:
    print("Duong den truong qua xa. Thoi! di xe may")
elif x >=300 and x <=700:
    print("Duong den truong khong xa. Thoi! di xe dap")
else:
    print("Khong xac dinh")