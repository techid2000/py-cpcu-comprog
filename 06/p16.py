s=list(map(int,input().strip().split(', ')))
le = len(s)
cnt = 0
for i in range(le):
    if(s[i]<0 and (i==le-1 or s[i+1]>=0)):
        cnt+=1  
print(cnt)