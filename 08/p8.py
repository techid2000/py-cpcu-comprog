d = {}
while True :
    s = input().strip().split()
    if s[0] == '-1' : break
    ls = len(s)
    d[s[0]] = []
    for i in range(1,ls) :
        d[s[0]].append(s[i])
s1,s2 = input().strip().split()
ans1 = 0
ans2 = 0
for c in d :
    if s1 in d[c] and s2 in d[c] : ans1 += 1
    elif s1 in d[c] or s2 in d[c] :ans2 += 1
print(ans1,ans2,ans1+ans2)