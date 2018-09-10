fi=open(input(),"r")
dic=dict()
i=0
for li in fi :
    if(i==0) :
        a=li.strip()
        if(a=="T2M") :
            a=1
        elif(a=="M2T") :
            a=2
        else :
            print("Invalid code")
            break
    elif(i==1) :
        b=li.strip()
        idx1=0
        while(True) :
            idx2=b.find("]",idx1)
            if(idx2==-1) :
                break
            cha=b[idx1+1:idx2]
            idx1=b.find("[",idx2)
            mos=b[idx2+1:idx1]
            if a==1 :
                dic[cha]=mos
            else :
                dic[mos]=cha
    else :
        ans=""
        ch=False
        if a==1 :
            b=li.strip()
            for c in b :
                if c in dic :
                    ans+=dic[c]+" "
                else :
                    ch=True
                    break
        if a==2 :
            b=li.strip().split()
            for c in b :
                if c in dic :
                    ans+=dic[c]
                else :
                    ch=True
                    break
        if(ch) :
            print("Invalid :",li)
        else :
            print(ans)
    i+=1