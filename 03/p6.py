n,y=map(int,input().split())
cnt=0
for x in range(n):
    k=int(input())
    if(k==y):cnt=cnt+1
print(cnt)