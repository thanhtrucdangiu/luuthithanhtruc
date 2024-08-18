# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 10:02:09 2024

@author: Student
"""
x=float(input("So quang duong di duoc (km): "))
if x <= 1:
    st=20
    print("Tong tien: ", st)
elif x<=3:
    st=x*13
    print("Tong tien: ",st)
elif x<=8:
    st=3*13+(x-3)*12
    print("Tong tien: ",st)
else:
    st= 3*13+5*12+(x-8)*10
    if x > 100:
        s1=st*0.92
        print("Tong tien: ",s1)
    else:
        print("Tong tien: ",st)