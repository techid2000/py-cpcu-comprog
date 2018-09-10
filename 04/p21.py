s={}
t={}
n=int(input())
pf = 0; sf = 0
S=''
for i in range(n):
    S = input()
    p = s; ch = False
    pf = 0
    for j in S:
        if(j not in p):p[j] = {}
        if(len(p)==1 and not ch):pf = pf+1
        elif(len(p)>1):ch=True
        p = p[j]

    p = t; ch = False
    sf = 0
    for j in reversed(S):
        if(j not in p):p[j]={}
        if(len(p)==1 and not ch):sf = sf+1
        elif(len(p)>1):ch = True
        p=p[j]
if(pf > 0): print(S[0:pf])
else: print('NO COMMON PREFIX')
if(sf > 0): print(S[len(S)-sf:len(S)])
else: print('NO COMMON SUFFIX')
