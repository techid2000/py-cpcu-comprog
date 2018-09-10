n=int(input())
r=n//2
for i in range(r):
    for j in range(r-i-1):
        print('.',end='')
    if(n%2==1):
        for j in range(i*2+3):
            print('#',end='')
    else:
        for j in range(i*2+2):
            print('#',end='')
    for j in range(2*(r-i)-1):
        print('.',end='')
    if(n%2==1):
        for j in range(i*2+3):
            print('#',end='')
    else:
        for j in range(i*2+2):
            print('#',end='')
    for j in range(r-i-1):
        print('.',end='')
    print()
for i in range(n//2-2):
    for j in range(2*n + 1):
        print('#',end='')
    print()
for i in range(n+1):
    for j in range(i):
        print('.',end='')
    for j in range(2*(n-i)+1):
        print('#',end='')
    for j in range(i):
        print('.',end='')
    print()