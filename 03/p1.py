s = 0
while True:
    a = int(input())
    if(a % 2 == 0):
        s = s + a
    if(a == -1):
        break
print(s)