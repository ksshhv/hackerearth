x=input()
while(int(x)):
    a=list(input())
    b=list(input())
    #print(a)
    #print(b)
    la=len(a)
    lb=len(b)
    k=0
    if(la<lb):
        for i in range(la):
            if a[i] in b:
                k=k+1
                gh=b.index(a[i])
                b[gh]='0'
    else:
        for j in range(lb):
            if b[j] in a:
                k=k+1
                gh=a.index(b[j])
                a[gh]='0'
    print(la+lb-2*k)
    x=int(x)-1
