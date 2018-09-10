a=[31,28,31,30,31,30,31,31,30,31,30,31]
x,y = map(int,input().split())
y = y - 543
if(x == 2):
    if((y%4==0 and y%100!=0) or y%400==0):
        a[1] = a[1]+1
print(a[x-1])