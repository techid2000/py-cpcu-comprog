n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
l=len(a)
pre = {}
for i in range(l):
   for j in range(i+1,l):
      if((a[i]+a[j]) in pre): pre[a[i]+a[j]] = max(pre[a[i]+a[j]], i)
      else: pre[a[i]+a[j]] = i
for q in b:
   ok=False
   for i in range(l):
      if(q-a[i] in pre and pre[q-a[i]] > i):
         print("YES")
         ok=True
         break
   if(not ok):
      print("NO")