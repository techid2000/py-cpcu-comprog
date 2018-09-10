from math import sqrt
a,b,c=map(int,input().split())
p=(a+b+c)/2
print(sqrt(p*(p-a)*(p-b)*(p-c)))