from math import factorial,pow
x = float(input())
k = 0
s = 0
while True:
    term = pow(-1,k)*pow(x,2*k)/factorial(2*k)
    if(abs(term) < pow(10,-8)):
        break
    k = k+1
    s = s + term
print(s,k-1)
    