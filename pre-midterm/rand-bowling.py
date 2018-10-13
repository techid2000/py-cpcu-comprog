from random import randint
mode=0
for i in range(5):
    mode=randint(0,2)
    if(mode==0):
        r=randint(0,9)
        rr=randint(0,9-r)
        print(r,rr,end=' ')
    elif(mode==1):
        r=randint(0,9)
        print(r,10-r,end=' ')
    else:
        print(10,end=' ')
    # print("/",end='')
if(mode>=1):
    r=randint(0,10)
    print(r,end=' ')
if(mode==2):
    r=randint(0,10)
    print(r,end=' ')
