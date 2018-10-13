from random import randint
a=['A','T','C','G']
v=100
while(v>0):
    w=randint(1,min(v,5))
    r=randint(0,3)
    rr=randint(0,1)
    if(rr==0):
        print(a[r],end='')
    else:
        print(a[r].lower(),end='')
    if(w>1):
        print(w,end='')
    v-=w