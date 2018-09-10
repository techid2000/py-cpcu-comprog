d,m,y = map(int,input().split())
opr = input()
day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
def time(x) :
    switcher = {
        'E' : 1,
        'Q' : 3,
        'N' : 7,
        'F' : 14
    }
    return switcher.get(x)

if y >=2558 :
    yy = y-543
    if yy % 400 == 0 or (yy % 4 == 0 and yy % 100 != 0) :
        day[2] = 29
if y < 2558 :
    print("Invalid year")
    exit(0)
elif not 1 <= m <= 12 :
    print("Invalid month")
    exit(0)
elif d > day[m] or d <= 0:
    print("Invalid date")
    exit(0)
elif opr not in "EQNF" :
    print("Invalid delivery type")
    exit(0)

if time(opr) + d > day[m] :
    d = time(opr) + d - day[m]
    m+=1
    if m == 13 :
        m = 1
        y += 1
else:
    d += time(opr)
print("delivered on %d/%d/%d"%(d,m,y))