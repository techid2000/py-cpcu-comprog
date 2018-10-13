s=input()
s=s.upper()
l=len(s)
index = []
for i in range(l):
    if(s[i].isalpha()):
        index.append(i)
index.append(l)
L=len(index)
for i in range(L-1):
    times = 1
    if(not(index[i]==l-1 or index[i]+1==index[i+1])):
        times = int(s[index[i]+1:index[i+1]])
    print(s[index[i]]*times,end='')
