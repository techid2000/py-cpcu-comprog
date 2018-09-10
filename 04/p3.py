s=input()
V=0
C=0
for c in s:
    if(c in 'aeiouAEIOU'):
        V+=1
    elif(c.isalpha()):
        C+=1
print(V,C)