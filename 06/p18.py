s={}
n=int(input())
for i in range(n):
    m=int(input())
    s[i+1]=m
a=1
while(True):
    print(a,end=' ')
    a=s[a]
    if(a==1): break