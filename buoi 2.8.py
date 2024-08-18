# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 09:37:27 2024

@author: Student
"""
a=float(input("Nhap he so a: "))
b=float(input("Nhap he so b: "))
c=float(input("Nhap he so c: "))
if a+b>c and a+c>b and b+c>a:
   
    if a==b==c:
        print("Tam giac deu.")
    elif a==b or a==b or b==c:
        print("Tam giac can.")
    if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print("Tam giac vuong")
else:
    print("Khong xac dinh")
        
