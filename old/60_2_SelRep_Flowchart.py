s = input().strip()
n = int(input())
if len(s) % n != 0 :
    print("ERROR")
    exit(0)
w = len(s)//n
x = ""
j = 0
while j < w :
    b = 0
    i = 0
    while i < n :
        k2 = i*w+j
        if not (str.isalpha(s[k2]) and str.islower(s[k2])) :
            b = 1
            break
        else :
            i += 1
    x += str(b)
    j += 1
j = w-1
while j >= 0 :
    if x[j] == "0" :
        t = ""
        i = 0
        while i < n :
            k1 = i*w
            k2 = k1+j
            k3 = (i+1)*w
            t += s[k1:k2]
            t += s[k2+1:k3]
            i +=1
        s = t
        w = w-1
    j = j-1
print(s)