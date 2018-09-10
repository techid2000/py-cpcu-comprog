s=input()
sa=input()
sb=input()
l=len(sa)
k={}
for i in range(l):
    k[sa[i]]=sb[i]
    k[sb[i]]=sa[i]
for c in s:
    if(c in k):
        print(k[c],end='')
    else:
        print(c,end='')