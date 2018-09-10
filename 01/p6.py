from math import cos,radians,sqrt
a=float(input())
b=float(input())
C=radians(float(input()))
print("c =",sqrt(a*a+b*b-2*a*b*cos(C)),"cm.")