//wrong approached, skip this!
from random import randint as rdi
n=int(input())
m=int(input())
a=[[0]*n for x in range(n)]
d=[(0,0),(0,-1),(-1,0),(-1,-1)]
for i in range(n):
    for j in range(n):
        a[i][j] = rdi(0,m)
for i in range(n-1,0,-1):
    for j in range(n-1,0,-1):
        cn = 0
        for k in d:
            x,y = i+k[0],j+k[1]
            if(a[x][y]=='x'):
                cn = 1
                break
        if(cn==0):
            k=d[rdi(0,3)]
            a[i+k[0]][j+k[1]]='x'
f=open("case_repair.txt",'w')
f.write(str(n)+'\n')
for i in range(n):
    for j in range(n):
        f.write(str(a[i][j])+' ')
f.write('\n')
f.close()