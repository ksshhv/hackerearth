x=int(input())
while(x):
    y=list(input())
    z=len(y)
    a=0
    while(z>0):
        a+=z
        z-=1
    print(a)
    x-=1
