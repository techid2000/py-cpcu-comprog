from math import ceil
h1 = int(input())
m1 = int(input())
h2 = int(input())
m2 = int(input())

m1 += h1*60
m2 += h2*60

d = m2-m1
h = int(ceil(d/60))
if(d <= 15):
    print(0)
elif(h > 6):
    print(200)
else:
    if(h <= 3):
        print(h*10)
    else:
        print(3*10 + (h-3)*20)


