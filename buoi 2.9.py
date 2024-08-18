# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:02:09 2024

@author: Student
"""
x=float(input("So quang duong di duoc (km): "))
if x == 1:
    print("Tong tien: ",20,"k")
elif a<=3:
    print("Tong tien: ", a*13, "k")
elif a<=8:
    print("Tong tien: ", 3*13+(a-3)*12,"k")
else:
    b= 3*13+5*12+(a-8)*10
    if b <= 100:
        print("Tong tien: ", b,"k")
    else:
        print("Tong tien: ", b*0.92, "k")