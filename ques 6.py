x=int(input())
while(x):
    y=int(input())
    l=1
    while(y):
        k=y-1
        while(k):
            print(" ",end="")
            k-=1
        m=l
        while(m):
            print("*",end="")
            m-=1
        print()
        l=l+2
        y-=1
    x-=1
