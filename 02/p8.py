a=[31,28,31,30,31,30,31,31,30,31,30,31]
n = int(input())
x = int(input())
y = int(input())
y = y - 543
s = 0
if((y%4==0 and y%100!=0) or y%400==0):
    a[1] = a[1]+1
for k in range(x-1):
    s = s + a[k]
print(s+n)
