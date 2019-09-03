x,y =input().split()
x=int(x)
y=int(y)
l=list(map(int,input().split()))
while(y):
    d=list(map(int,input().split()))
    if(d[0]==1):
        if(l[d[1]-1]==0):
            l[d[1]-1]=1
        else:
            l[d[1]-1]=0
    else:
        if(l[d[2]-1]==0):
            print("EVEN")
        else:
            print("ODD")
    y-=1
