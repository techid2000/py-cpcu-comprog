file = "data.txt"
n=input()
f = open(file,"r")
s=0
cnt=0
for l in f:
    a=l.split(':')
    if(a[2]==n):
        s+=float(a[3]); cnt+=1
if(cnt==0):
    print("Not Found")
else:
    print(s/cnt)
