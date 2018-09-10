def f(x, y):
    if(x == 0):
        return
    f(x//y, y)
    print(x % y,end='')

a,b = map(int,input().split())
if(a < 0 or b > 9 or b < 2):
    print('Error: Cannot convert')
else:
    f(a,b)