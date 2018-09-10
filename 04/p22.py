m=['zero','one','two','three','four','five','six','seven','eight','nine']
s=input()
l=len(s)
for c in range(l):
    if(s[c].isnumeric()):
        print(m[int(s[c])],end='')
        if(c+1<l and s[c+1].isalnum()):
            print('',end=' ')
    else:
        print(s[c],end='')
