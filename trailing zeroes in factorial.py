x=int(input())
while(x):
    y=int(input())
    z=0
    b=5
    while(z<y):
        a=b
        while(a>=5):
            if(a%5==0):
                a=a/5
                z=z+1
            else:
                break
        b+=5
        #print(b)
    #print(z)
    if(z!=y):
        print("0")
    else:
        print("5")
        print(""+str(b-5)+" "+str(b-4)+" "+str(b-3)+" "+str(b-2)+" "+str(b-1))
    x-=1
