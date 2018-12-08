warp,ok,path,paths={},False,[],[]
w,c,d=[int(x) for x in input().split()]
def f(u):
    path.append(u)
    if(u==d):
        paths.append(path[:])
        path.pop(-1)
        return
    if(u in warp):
        for v in warp[u]:
            f(v)
    path.pop(-1)
for i in range(w):
    x,y=[int(x) for x in input().split()]
    warp[x] = {y} if not x in warp else warp[x] | {y}
f(c)
if (len(paths) > 0): 
    paths.sort()
    for a in paths:
        for i in range(len(a)):
            if(i > 0): print('->',end=' ')
            print(a[i],end=' ')
        print()
else:
    print('no')