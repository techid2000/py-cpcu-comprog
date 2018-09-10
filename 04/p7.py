a=[0]*10
s=input()
for i in s:
    a[int(i)]+=1
ch=True
for i in range(10):
    if(a[i]==0):
        print(i,end=' ')
        ch=False
if(ch):
    print('No missing digits')