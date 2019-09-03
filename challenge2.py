from fractions import Fraction
a=int(input())
while(a):
    x,y,z=input().split()
    x=int(x)
    y=int(y)
    z=int(z)
    q=[2,3,5,7,11,13,17,19,23]
    bs=0
    l=0
    m=0
    while(x<24):
        bs=0
        for i in q:
            if(x%i==0 and y%i==0 and z%i==0):
                bs+=1
        if(bs==0):
            l+=1
        else:
            m+=1
        if(z<59):
            z+=1
        else:
            z=0
            if(y<59):
                y+=1
            else:
                y=0
                x+=1
    a-=1
    k=str(Fraction(m, l))
    k1,k2=k.split("/")
    print(str(k1)+":"+str(k2))
