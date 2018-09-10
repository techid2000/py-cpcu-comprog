n,t=map(int,input().split())
for i in range(n):
    for j in range(n):
        if((i <= j and t == 1) or (i+j+1==n and t == 3) or (i >= j and t == 2)): 
            print('('+str(i+1)+','+str(j+1)+')')