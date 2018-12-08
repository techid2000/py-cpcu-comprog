def fac(n):
    return str(n)+'!'
def oneterm(x,n):
    return x if str(n) == '1' else x+'**'+str(n)+'/'+fac(n)
def sine(x,n):
    ret = ''
    for i in range(1,int(n)+1):
        if(i > 1):
            ret += ('-' if i%2==0 else '+')+' '
        ret += oneterm(x,2*i-1)+' '
    return ret
ln=input().replace(' ','')
if(ln[6]=='f'):
    a = int(ln[10:-2])
    print(fac(a))
elif(ln[6]=='o'):
    a,b = ln[14:-2].split(',')
    print(oneterm(a,b))
elif(ln[6]=='s'):
    a,b = ln[10:-2].split(',')
    print(sine(a,b))
