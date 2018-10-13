l=[]
while(True):
    s=input()
    if(s[0]=='r'):
        l.append(s[7:])
        print(len(l))
    elif(s[0]=='l'):
        print(l)
    elif(s[0]=='s'):
        if(len(l)==0): print('no book')
        else: print(l.pop(-1))
    elif(s[0]=='t'):
        if(len(l)==0): print('no book')
        else: print(l[len(l)-1])
    elif(s[0]=='e'):
        break
