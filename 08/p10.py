n=int(input())
ntok=dict()
nl=list()
ch=0
for i in range(n):
    num,key=input().split(":")
    for j in key.split(","):
        j=j.strip()
        num=num.strip()
        if num not in ntok:
            ntok[num]=set()
        ntok[num].add(j)
    nl.append(num)
q=input().strip()
if q in ntok:
    for i in range(n):
        if nl[i]!=q and len(ntok[nl[i]].intersection(ntok[q]))!=0:
                print(nl[i])
                ch=1
if ch==0:
    print("Not Found")