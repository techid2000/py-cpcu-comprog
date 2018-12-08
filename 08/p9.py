n=int(input())
aa=dict()
for i in range(n):
    a,b,c,d,e=[e for e in input().split(', ')]
    if b not in aa:
        aa[b]=[]
    aa[b].append(a)
    if c not in aa:
        aa[c]=[]
    aa[c].append(a)
    if d not in aa:
        aa[d]=[]
    aa[d].append(a)
    if e not in aa:
        aa[e]=[]
    aa[e].append(a)
for i in input().split(', '):
    s=""
    s=s+i+" -> "
    if i not in aa:
        s=s+"Not found"
    else:
        for k in aa[i]:
             s=s+k+", "
        s=s[:-2]
    print(s)