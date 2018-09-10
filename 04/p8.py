s=input()
a,b=map(int,input().split())
print(s[:a],end='')
for i in reversed(range(a,b+1)):
    print(s[i],end='')
print(s[b+1:],end='')