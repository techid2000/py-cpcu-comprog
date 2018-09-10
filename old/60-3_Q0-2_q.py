x1,x2,x3,x4,x5=map(int,input().split())
if(x1>x2):
    if(x2<x3):
        print("C4")
    if(x3<x4):
        print("C5")
    if(x4<x5):
        print("C6")
    print("C7")
else:
    if(x2>x3):
        if(not x3<x5):
            print("C2")
    else:
        if(x4<x5):
            print("C1")
    print("C3")
