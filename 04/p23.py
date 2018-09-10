hst=input()
ndl=input()
hst=hst.replace('.','')
hst=hst.replace(',','')
hst=hst.replace('"','')
hst=hst.replace('\'','')
hst=hst.lower()
ndl=ndl.lower()
for x in list(hst.split(' ')):
    if(x == ndl):
        print("Found")
        exit(0)
print("Not Found")   