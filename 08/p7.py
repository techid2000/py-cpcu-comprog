n=int(input())
m={}
bo=[]
ma=0
for i in range(n):
   a,b=input().split()
   k=b[0:2]
   if(k in m): m[k].append(b)
   else: m[k]=[b]
for i in m:
   ma=max(ma,len(m[i]))
for i in m:
   if(len(m[i])==ma):
      bo.append(i)
bo=sorted(bo)
print(bo[0])
print(ma)
for i in m[bo[0]]:
   print(i)