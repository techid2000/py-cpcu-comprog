a=list(map(int,input().split(' ')))
game=0
score=0
final=0
turn=0
i=0
while(i<len(a)):
    score+=a[i]
    if(game==5):
        break
    if(turn==0):
        if(score==10):
            final+=score
            game+=1
            if(i+1<len(a) and i+2<len(a)):
                final+=a[i+1]+a[i+2]
                if(game > 5):
                    print("ERROR"); exit(0)
            else:
                print("ERROR"); exit(0)
            score=0
        else:
            turn=1
    else:
        final+=score
        game+=1    
        if(score==10):
            if(i+1<len(a)):
                final+=a[i+1]
                if(game > 5):
                    print("ERROR"); exit(0)
            else:
                print("ERROR"); exit(0)
        elif(score>10):
            print("ERROR"); exit(0)
        turn = 0
        score=0
    i+=1
if(game!=5): print("ERROR"); exit(0)
else: print(final)