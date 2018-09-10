from math import sqrt
n=int(input())
sq = int(sqrt(n))
for x in range(2,sq+1):
    if(n % x == 0):
        print(x,end=' ')
        while(n % x == 0):
            n = n // x
if(n > 1):
    print(n)