# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:43:13 2024

@author: Student
"""
x= float(input("Nhap diem trung binh (GPA):"))
if x <3.5:
    print("Hoc luc kem")
elif 3.5<= x <5.0:
    print("Hoc luc yeu")
elif 5.0<= x <7.0:
    print("Hoc luc trung binh")
elif 7.0<= x <8.0:
    print("Hoc luc kha")
elif 8.0<= x <9.0:
    print("Hoc luc gioi")
elif 9.0<= x <=10:
    print("Hoc luc xuat sac")
else:
    print("Khong xac dinh")