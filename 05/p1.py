file = "score.txt"
n=input()
f = open(file,"r")
for l in f:
    a=l.split()[0]
    b=l.split()[1]
    if(a==n):
        print(b)
        exit(0)
print('Not Found')