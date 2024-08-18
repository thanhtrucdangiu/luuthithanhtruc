# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 08:05:37 2024

@author: Student
"""
a= float(input("Nhap he so a:"))
b= float(input("Nhap he so b:"))

if a == 0:
    if b == 0:
        print("Phuong trinh co vo so nghiem.")
    else:
        print("Phuong trinh vo nghiem.")
else:
    x = -b/a
    print(f"Nghiem cua phuong trinh la x = {x}")
         