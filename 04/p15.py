s=input()
s=s.lower()
l=len(s)
cnt=0
mx=0
for c in range(l):
    if(c==0 or s[c] != s[c-1]):
        cnt=0
    cnt = cnt+1
    mx = max(mx, cnt)
print(mx)