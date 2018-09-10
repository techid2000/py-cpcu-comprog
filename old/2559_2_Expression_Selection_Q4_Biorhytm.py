from math import sin,pi
D=[0,31,28,31,30,31,30,31,31,30,31,30,31]
bd,bm,by,d,m,y=map(int,input().split())
by-=543
y-=543
red=0
if((by%4==0 and by%100!=0) or by%400==0):D[2]=29
else:D[2]=28
red+=D[bm]-bd+1
for i in range(bm+1,13):red+=D[i]
black = (y-by-1)*365
if((y%4==0 and y%100!=0) or y%400==0):D[2]=29
else:D[2]=28
blue=0
for i in range(1,m):blue+=D[i]
blue+=d-1
t = red+black+blue
print(t,"{:.2f}".format(sin(2*pi*t/23)),"{:.2f}".format(sin(2*pi*t/28)),"{:.2f}".format(sin(2*pi*t/33)))