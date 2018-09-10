a,b=input().split()
print(a[0].upper(),end='')
for i in range(1,len(a)):
    print(a[i].lower(),end='')
s = 0
for i in range(len(b)):
    if(b[i].isnumeric()):
        s+=int(b[i])
print(' '+str(s))