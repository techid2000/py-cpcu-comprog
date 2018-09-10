s=input()
for y in range(10):
    k = 10
    sum = 0
    for x in s:
        sum += int(x)*k
        k -= 1
    if((sum + y) % 11 == 0):
        print(s+str(y))
        break