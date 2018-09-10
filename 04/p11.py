s=input()
cnt=0
for c in s:
    if(c=='1'):
        cnt+=1
print(s,end='')
if(cnt % 2 == 1):
    print('1')
else:
    print('0')