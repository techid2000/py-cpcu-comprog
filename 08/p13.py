f1=open('file1.txt')
f2=open('file2.txt')
s1=""
s2=""
se1=set()
se2=set()
for line in f1:
    lin=str(line)
    for i in range(len(lin)):
        if """‘“-.(),""".find(lin[i])!=-1 or lin[i]==" ":
            if(len(s1)!=0):
                se1.add(s1.lower())
            s1=""
        elif lin[i] != "\n":
            s1 = s1+ lin[i]
    if (len(s1) != 0):
        se1.add(s1.lower())
    s1 = ""
for line in f2:
    lin = str(line)
    for i in range(len(lin)):
        if """‘“-.(),""".find(lin[i])!=-1 or lin[i]==" ":
            if (len(s2)!=0):
                se2.add(s2.lower())
            s2=""
        elif lin[i]!="\n":
            s2=s2+lin[i]
    if (len(s2) != 0):
        se2.add(s2.lower())
    s2 = ""
k=input().lower()
if k in se1:
    if k in se2:
        print("Found in both files")
    else:
        print("Found in file1 only")
else:
    if k in se2:
        print("Found in file2 only")
    else:
        print("Not found")

