a=list(map(int,input().split()))
t=0
x=0
y=0
while(len(a)>0):
    if(t==0): x+=a.pop(a.index(max(a[0],a[-1])))
    else: y+=a.pop(a.index(max(a[0],a[-1])))
    t=1-t
print(x)
print(y)
if(x>y):print(1)
elif(x<y):print(2)
else:print(0)
