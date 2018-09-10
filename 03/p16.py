from math import sqrt
n=int(input())
sq=int(sqrt(n))
ok=False
for x in range(0,sq+1):
    for y in range(x,sq+1):
        if(x*x + y*y == n):
            print(x,y)
            ok=True
if(not ok):
    print('No solution')
