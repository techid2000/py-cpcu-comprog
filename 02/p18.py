a,b,c=map(int,input().split())
d,e,f=map(int,input().split())

D = a*e - b*d
D1 = -c*e + f*b
D2 = -a*f + c*d

if(D1 == 0 and D2 == 0 and D == 0 ):
    print('many solutions')
elif(D == 0):
    print('no solution')
else:
    print('one solution')