s=input()
a=input()
b=input()
for c in s:
    if(c==a): print(b,end='')
    elif(c==b): print(a,end='')
    else: print(c,end='')