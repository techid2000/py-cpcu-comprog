a = sorted([int(x) for x in input().split()])
b = int(input())
cnt = 0
mem = {}
for x in a:
   mem[x] = mem[x]+1 if x in mem else 1   
for x in mem:
   if(b-x < x and b-x in mem): cnt += mem[x]*mem[b-x]
   elif(b-x == x): cnt += mem[x]*(mem[x]-1)//2
print(cnt)