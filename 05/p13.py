file=input()
f=open(file,"r")
t=int(input())
a=input()
a=a.upper()
b=input()
la=len(a)
for l in f:
    L=l.upper()
    k=0
    ll=len(l)
    while(k<ll):
        if(L[k:k+la]==a and t>0):
            print(b,end='')
            k+=la
            t-=1
        else:
            print(l[k],end='')
            k+=1
    print()