A={'soon':0,'nueng':1,'ed':1,'song':2,'yee':2,'sam':3,'see':4,'ha':5,'hok':6,'jed':7,'pad':8,'kao':9}
B={'sip':10,'roey':100,'pun':1000,'muen':10000,'saen':100000,'larn':1000000}
def pr(x,y):
    if(x==0): 
        if(y==0):
            print(0,end='')
        return
    pr(x//10,y+1)
    print(x%10,end='')
    if(y%3==0 and y>0):
        print(',',end='')
exp=input()
sp=list(exp.split('-'))
if(sp[0]=='lop'):
    print('-',end='')
    sp=sp[1:]
value = 0
i=0
l=len(sp)

while(i<l and sp[i]!='jood'):
    if(sp[i]=='sip' and (i==0 or not A.__contains__(sp[i-1]))):
        value += 10; i+=1
    elif(sp[i]=='larn'):
        value*=B['larn']; i+=1
    elif(i==l-1 or sp[i+1]=='jood' or sp[i+1]=='larn'):
        value += A[sp[i]]; i+=1
    else:
        value += A[sp[i]]*B[sp[i+1]]; i+=2
pr(value,0)
while(i<l):
    if(sp[i]=='jood'):print('.',end='')
    else:print(A[sp[i]],end='')
    i=i+1