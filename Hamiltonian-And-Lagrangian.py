x=int(input())
y=0
l=list(map(int,input().split()))
while(y<x):
    k=y
    s=0
    while(k<x):
        if(l[k]>l[y]):
            s=1
            break
        k+=1
    if(s==0):
        print(l[y],end=" ")
    y+=1
