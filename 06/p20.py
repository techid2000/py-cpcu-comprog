from math import floor
tb=[]
s=list(map(int,input().strip().split()))
ls=len(s)
su = 0
tb.append(s)
for i in range(floor(ls/2)):
    s=list(map(int,input().strip().split()))
    tb.append(s)
for i in range(len(tb)):
    for j in range(floor(ls/2)-i,floor(ls/2+i+1)):
        su += tb[i][j]
print(su)

