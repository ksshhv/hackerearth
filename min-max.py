x=input()
y=list(map(str,input().split()))
y=sorted(y)
a=1
d=0
b=int(y[0])
while(a<len(y)):
    if(int(y[a])==b or int(y[a])==b+1):
        b=int(y[a])
        a=a+1
        continue
    else:
        d=d+1
        print("NO")
        break
if(d==0):
    print("YES")
    
       
