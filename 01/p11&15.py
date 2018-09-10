h1=int(input())
m1=int(input())
s1=int(input())
h2=int(input())
m2=int(input())
s2=int(input())
a=h1*3600+m1*60+s1
b=h2*3600+m2*60+s2
c=(b-a)%(24*3600)
if(c<0): c+=(24*3600)
print(str(c//3600)+":"+str((c%3600//60))+":"+str((c%3600%60)))