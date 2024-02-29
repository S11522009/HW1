# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import cmath
a=float(input("a值:"))
b=float(input("b值:"))
c=float(input("c值:"))

discriminant=b**-4*a*c

root1=(-b+cmath.sqrt(discriminant))/(2*a)
root2=(-b-cmath.sqrt(discriminant))/(2*a)

print(f"解為:{root1}和{root2}")
