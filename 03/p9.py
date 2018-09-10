n=int(input())
ch=False
for x in range(n-1,1,-1):
    if(n%x==0):
        print(x,end=' ')
        ch=True
if(not ch):
    print('Prime Number')