s = input()
a = 13
sum = 0
for c in s:
    sum += int(c)*a
    a = a-1
print((11-(sum)%11)%10)