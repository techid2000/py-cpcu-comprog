fl1=input()
fl2=input()
f1=open(fl1,"r")
f2=open(fl2,"r")
l2 = [0]
for l in f2:
    l2.append(l2[len(l2)-1]+float(l))
la = 0
for l in f1:
    print((l2[int(l)+la]-l2[la])/int(l))
    la = int(l)+la
