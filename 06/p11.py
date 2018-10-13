fn=input().strip()
o = open(fn,"r")
mp={}
for i in o:
    if(i.strip()==''):continue
    k=list(i.strip().split(';'))
    k[1]+=' '+k[2]; k.pop(2)
    y=float(k.pop(-1))
    k[-1]=float(k[-1])+y
    g=''
    if(k[-1]>=80): g='A'
    elif(k[-1]>=70): g='B'
    elif(k[-1]>=60): g='C'
    elif(k[-1]>=50): g='D'
    else: g='F'
    k.pop(-1); k.append(g)
    if(not(k[0] in mp)):
        mp[k[0]]=k
while(True):
    id=input().strip()
    if(id=='-1'):
        break
    if(id in mp):
        print(mp[id])
    else:
        print('Not Found')