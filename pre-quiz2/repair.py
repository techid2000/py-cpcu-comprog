n=int(input())
a = [x for x in input().split()]
b = [a[n*x:n*x+n] for x in range(n)]
d = {(0,0),(0,1),(1,0),(1,1)}
for i in range(n-1):
    for j in range(n-1):
        s,p,q = set(),-1,-1
        for k in d:
            x,y = i+k[0],j+k[1]
            if(b[x][y] == 'x'): p,q = x,y
            else: s.add(int(b[x][y]))
        if(p>=0 and q>=0): b[p][q]=sum(s)//len(s)
for i in range(n):
    for j in range(n):
        print(b[i][j],end=' ')
    print()