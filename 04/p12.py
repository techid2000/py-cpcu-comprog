s1=input()
s2=input()
if( sorted(s1.replace(' ','').lower())==sorted(s2.replace(' ','').lower())):
    print(s1)
else:
    print(s1,s2)