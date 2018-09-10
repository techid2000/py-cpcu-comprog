s=input()
s=s.replace(' ','')
s=s.upper()
def f(x, y):
    if(x>=y): return 'yes'
    if(s[x]!=s[y]): return 'no'
    return f(x+1, y-1)
print(f(0, len(s)-1))