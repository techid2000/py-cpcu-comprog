import string
appear={}
S=''
s=input()
for c in s:
    if(c not in appear):appear[c]=0
    appear[c]+=1
    if(appear[c] <= 2):
        if(appear[c]==2):
            S = S.replace(c,'')
        S += c
print(S)
