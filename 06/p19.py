fn=input().strip()
f=open(fn,'r')
m={}
res=[]
ma = 0
ty = ''
for l in f:
    a,b=l.strip().split()
    if not a in m:
        m[a]=[]
    m[a].append(b)
for i in m:
    res.append([i,m[i]])
    if(len(m[i]) > ma):
        ma = len(m[i])
        ty = i
print(res)
print('The most favorite fruit is',ty)