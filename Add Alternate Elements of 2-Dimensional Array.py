x=list(map(int,input().split()))
y=0
a=0
b=0
while(y<len(x)):
    if(y%2==0):
        a+=x[y]
    else:
        b+=x[y]
    y+=1
print(a)
print(b)
