file=input()
f=open(file,"r")
be=0
se=0
ve=0
et=0
for l in f:
    a=l.upper().split()[0]
    if(a=='BE'):
        be+=1
    if(a=='SE'):
        se+=1
    if(a=='VE'):
        ve+=1
    if(a=='ET'):
        et+=1
print(be,se,ve,et,be+se+ve+et)