l1 = input().split()
l2 = input().split()
ca,a = int(l1[0]),int(l1[1])
cb,b = int(l2[0]),int(l2[1])
if(a+b > cb):
    print(a-(cb-b),cb)
else:
    print(0,a+b)