from math import sqrt
p=int(input())
ans = 0
for a in range(p-1):
    A = a+1
    x = (p*p - 2*A*p)/(2*p-2*A)
    hyp = sqrt(x*x + A*A)
    if(x > 0 and round(x)==x and round(hyp)==hyp):
        ans = max(ans,int(hyp))
print(ans)