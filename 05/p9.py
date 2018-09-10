file=input()
f=open(file,"r")
s={}
for l in f:
    a=l[:10]
    if(a not in s):
        print(a)
        s[a]=1