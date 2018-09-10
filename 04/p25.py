exp=input()
symbol=[]
if(exp[0]=='-'): 
    symbol.append(-1)
    exp=exp[1:]
else:
    symbol.append(1)
    if(exp[0]=='+'):
        exp=exp[1:]
l = len(exp)
for c in range(l):
    if(exp[c] == '-'): symbol.append(-1)
    elif(exp[c]=='+'): symbol.append(1)
exp = exp.replace('-','+')
nums = list(map(int,exp.split('+')))
s = 0
l = len(nums)
for i in range(l):
    s += symbol[i] * nums[i]
print(s)