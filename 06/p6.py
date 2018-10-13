n=int(input())
a=[0]
for i in range(n):
    m=int(input())
    a.append(m+a[len(a)-1])
x,y=map(int,input().split())
print(a[y+1]-a[x])