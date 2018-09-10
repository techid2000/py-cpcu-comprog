a1,b1,c1=map(float,input().split())
a2,b2,c2=map(float,input().split())

d=a1*b2 - a2*b1
d1=-c2*a1 + a2*c1
d2=-c1*b2 + c2*b1
print(d2/d,d1/d)