x=int(input())
while(x):
    y=input()
    z=0
    min=100000000
    max=0
    while(z<len(y)):
        if(int(y[z])< min):
            min=int(y[z])
        if(int(y[z])>max):
            max=int(y[z])
        z+=1
    m=1
    key=0
    while(m<len(y)):
        if(y[m]==y[m-1]):
            key=1
            break
        m+=1
    if(max-min+1==len(y) and key==0):
        print("YES")
    else:
        print("NO")
    x-=1
