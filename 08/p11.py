f = open("books.txt")
s = input().strip().split(', ')
ans = []
for li in f :
    x = li.strip().split(', ')
    ch = True
    for c in s :
        if c not in x[1:] :
            ch = False
            break
    if ch : ans.append(x[0])
f.close()
if len(ans) == 0 : print("Not found")
else :
    for c in ans : print(c)