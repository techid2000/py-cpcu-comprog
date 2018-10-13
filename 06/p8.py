s=list(input())
n=int(input())
for i in range(n):
    cm=list(input().split())
    if(cm[0]=="in"):
        s.insert(int(cm[2]),cm[1])
    elif(cm[0]=="out"):
        s.pop(int(cm[1]))
    elif(cm[0]=="swap"):
        tmp=s[int(cm[1])]
        s[int(cm[1])]=s[int(cm[2])]
        s[int(cm[2])]=tmp
    for j in s:
        print(j,end='')
    print()