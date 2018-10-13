n=int(input())
l=[]
for i in range(1,n+1):
    l.append(i)
while(True):
    x,y=map(int,input().split())
    if(x==0 and y==0): break
    p=l.index(x)
    q=l.index(y)
    tmp=l[p]
    l[p]=l[q]
    l[q]=tmp
print(l)