d=[int(i) for i in input().split()]
n = len(d)
for i in range(n):d[i]=float(d[i])
for k in range(n-1):
  for i in range(n-1):
    if d[i] > d[i+1]: 
      d[i],d[i+1] = d[i+1],d[i] 
if n%2:print(d[n//2])
else: print((d[n//2]+d[n//2-1])/2)