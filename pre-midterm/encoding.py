s=input()
l=len(s)
cnt=0
for i in range(l):
    cnt += 1
    if(i==l-1 or s[i+1].upper()!=s[i].upper()):
        print(s[i].upper(),end='')
        if(cnt>1):
            print(cnt,end='')
        cnt = 0