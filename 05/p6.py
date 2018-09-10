file = input()
f = open(file,"r")
g = 0
def F(x):
    if(x >= 80): return 'A'
    if(x >= 75): return 'B+'
    if(x >= 70): return 'B'
    if(x >= 65): return 'C+'
    if(x >= 60): return 'C'
    if(x >= 55): return 'D+'
    if(x >= 50): return 'D'
    return 'F'
for l in f:
    g = 0
    a=l.split()
    if(len(a)>1):
        for j in range(1,6):
            g+=int(a[j])
        print(a[0],F(g))