a=int(input())
if(a<0 or a>81):
    print('Error : Out of range')
else:
    print(str((a//3//3//3)%3)+str((a//3//3)%3)+str((a//3)%3)+str(a%3))