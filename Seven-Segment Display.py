def machis(x):
    y=int(x)
    if(y==6 or y==9 or y==0):
        return 6
    if(y==1):
        return 2
    if(y==2 or y==3 or y==5):
        return 5
    if(y==7):
        return 3
    if(y==4):
        return 4
    if(y==8):
        return 7
def maxm(x):
    y=int(x)
    if((y%2)==0):
        z=y/2
        while(z):
            print(1,end="")
            z-=1
    if((y%2)==1):
        print(7,end="")
        z=int(y/2)-1
        while(z):
            print(1,end="")
            z-=1
    print("")
a=int(input())
while(a):
    b=list(input())
    c=len(b)
    d=0
    while(c):
        d=d+machis(b[c-1])
        c-=1
    maxm(d)
    a-=1
    
