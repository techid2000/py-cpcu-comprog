mode=input()
s=input()
a=input()
b=input()
ss=s.upper()
a=a.upper()
lss=len(ss)
la=len(a)
ch=False
i=0
while(i<lss-la+1):
    if(ss[i:i+la]==a and ((mode=='R' and not ch) or mode=='RA')):
        print(b,end='')
        if(mode=='R'):
            ch=True
        i+=la
    else: print(s[i],end=''); i=i+1
while(i<lss):
    print(s[i],end='');i+=1
