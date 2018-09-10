from math import ceil
A= {0:'soon',
    1:'nueng',
    2:'song',
    3:'sam',
    4:'see',
    5:'ha',
    6:'hok',
    7:'jed',
    8:'pad',
    9:'kao'}
B= {10:'sip',
    100:'roey',
    1000:'pun',
    10000:'muen',
    100000:'saen',
    1000000:'larn'}
words = []
def f(x, y):
    if(x == 0):
        if(y == 1):
            words.append(A[0])
        return
    if(y == 1000000):
        f(x//10, 10)
    else:
        f(x//10, y*10)
    if(x%10==1):
        if(not y==10):
            if((y==1 or y==1000000) and x//10 > 0):
                words.append('ed')
            else:
                words.append('nueng')
    elif(x%10==2):
        if(y==10):
            words.append('yee')
        else:
            words.append('song')
    elif(x%10>2):
        words.append(A[x%10])
    if((x%10 > 0 and B.__contains__(y)) or y==1000000):
        words.append(B[y])
raw = input().replace(',','')
if(raw[0]=='-'):
    words.append('lop')
    raw=raw[1:]
sp = list(raw.split('.'))
f(int(sp[0]),1)
if(len(sp)>1):
    words.append('jood')
    for a in sp[1]:
        words.append(A[int(a)])
print(words[0],end='')
l = len(words)
for i in range(1,l):
    print('-'+words[i],end='')
    