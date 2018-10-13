from random import randint
a=['A','T','C','G']
for i in range(100):
    r=randint(0,3)
    rr=randint(0,1)
    if(rr==0):
        print(a[r],end='')
    else:
        print(a[r].lower(),end='')