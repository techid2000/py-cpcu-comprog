s = set()
wtf = input()
def yay(y, z):
    if(y == len(wtf)):
        if(z != ''): s.add(z)
        return
    yay(y+1, z+wtf[y])
    if(wtf[y].isupper()):
        yay(y+1, z)
yay(0, '')
l = sorted(list(s))
for ln in l: print(ln)