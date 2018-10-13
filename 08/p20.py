from operator import itemgetter as ig
n=int(input())
a=[]; A={}
nf=1
for i in range(n):
   b={}
   for j in input().split(): 
      b[j] = b[j]+1 if j in b else 1
   a.append(b)
c=input()
for i in a:
   if c in i:
      nf=0
      for j in i:
         if(j!=c): A[j]=A[j]+1 if j in A else 1
fin = []
for i in A:
   fin.append((i,A[i]))
fin = sorted(fin,key=ig(0))
fin = sorted(fin,key=ig(1),reverse=True)
if(nf):
   print("Not Found")
else:
   if(len(fin)==0):
      print("No suggested event")
   else:
      for i in fin:
         print(i[0],i[1])