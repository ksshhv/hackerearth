x=int(input())
y=0
z=7
while(x):
    a=int(input())
    if((z-a)<(a-y)):
        print("B")
        z=a
    else:
        print("A")
        y=a
    x-=1
    
