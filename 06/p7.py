s=input()
t=input()
s=list(map(int,s[1:-1].split(',')))
t=list(map(int,t[1:-1].split(',')))
sum=0
for i in range(len(s)):
    sum+=s[i]*t[i]
print(sum)