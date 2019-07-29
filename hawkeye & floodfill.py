x=int(input())
a,b,p=input().split()
a=int(a)
b=int(b)
p=int(p)
n=[]
y=x
e=0
while(e<x):
    m=[]
    f=0
    while(f<y):
        if(p<=abs(a-e) or p<=abs(b-f)):
            m.append("0")
        else:
            m.append(min(p-(abs(a-e)),p-(abs(b-f))))
        f+=1
    n.append(m)
    e+=1
k=0
while(k<x):
    l=0
    while(l<y):
        print(n[k][l],end=" ")
        l+=1
    print()
    k+=1
        
