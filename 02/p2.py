a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

t = 0
if(a > b):
    t = b 
    b = a
    a = t
if(c > d):
    t = d
    d = c
    c = t
if(b > e):
    t = e
    e = b
    b = t
if(d > e):
    t = e
    e = d
    d = t

if(a > b):
    t = b
    b = a
    a = t
if(c > d):
    t = d
    d = c
    c = t
if(b > d):
    t = d
    d = b
    b = t

if(a > c):
    t = c
    c = a
    a = t
if(b > c):
    t = c
    c = b
    b = t

print(c)
