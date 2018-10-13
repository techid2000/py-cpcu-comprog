a = input().split()
b = input().split()
d = {}
for i in range(len(a)) :
    d[a[i]] = b[i]
    d[b[i]] = a[i]
s = input().split()
for i in range(len(s)) :
    if s[i] in d :
        s[i] = d[s[i]]
print(' '.join(s))