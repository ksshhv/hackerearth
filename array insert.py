a,b=input().split()
x=list(map(str,input().split()))
while(int(b)>0):
    c,d,e=input().split()
    if(int(c)==1):
        
        x[int(d)]=e
    if(int(c)==2):
        if(int(d)>int(a)-1 or int(e)>int(a)-1):
            print("-1")
        else:
            j=0
            z=int(e)
            while(z>=int(d)):
                j=j+int(x[z])
                z=z-1
        print(j)
    b=int(b)-1
