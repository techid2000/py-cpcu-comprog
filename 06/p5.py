l=[]
a=0
while True:
    a=int(input())
    if(a < 0):
        break
    l.append(a)
for i in l:
    print(i+a)