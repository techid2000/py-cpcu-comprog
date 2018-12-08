from math import sqrt
def zscore(L):
    mean,sigma,ret=sum(L)/len(L),0,[]
    for x in L: sigma += (x - mean)*(x - mean)
    sd = sqrt(sigma/len(L))
    for x in L: ret.append((x-mean)/sd)
    return ret

L = [float(e) for e in input().split()]
for i in zscore(L):
    print(i)
#-2 -1 1 0 2