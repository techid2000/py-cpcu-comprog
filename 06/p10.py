fn=input()
l=[]
o = open(fn,"r")
for i in o:
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
    l.append(k)
print(l)