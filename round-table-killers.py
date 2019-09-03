n,k,x=input().split()
n=int(n)
k=int(k)
x=int(x)
a=["0"]
b=0
while(b<n):
    a.append("1")
    b+=1
def inc(t,m):
    if(t+1>m):
        t=1
    else:
        t=t+1
    return t
#print(inc(x,n))
while(a.count("1")>1):
    c=x%k
    if(c==0):
        x=inc(x,n)
    else:
        while(c>0):
            if(a.count("1")>1):
                
                x=inc(x,n)
                if(int(a[x])==1):
                    a[x]="0"
                    #print(c)
                    c=c-1
                    #print(a)
            else:
                break
        while(int(a[x])==0):
            x=inc(x,n)
            #print(x)
print(x)
