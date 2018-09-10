s=input()
l=len(s); cnt=0
for c in range(l):
    if(s[c] in "aeiou" and (c==l-1 or s[c+1] not in "aeiou")):
        cnt=cnt+1
print(cnt)