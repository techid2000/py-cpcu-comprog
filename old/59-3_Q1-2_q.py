a,b,c,d=map(int,input().split())
if(a > b):
    t=a; a=b; b=t
    if(d >= a):
        if(c > d):
            c = c-a
    else:
        c = c+a
    b=a+c+d
else:
    if(c > a and a>=b):
        d = d+a
    if(d > c):
        if(d % 2 == 0):
            b = b + 2
    else:
        b = 2*b
print(a,b,c,d)