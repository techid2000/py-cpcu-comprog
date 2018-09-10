n=0
s=0
while(True):
   k=float(input())
   if(k==-1):break
   s+=k
   n=n+1
if(n==0):print('No Data')
else:print(s/n) 