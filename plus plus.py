x,y=input().split()
x=int(x)
y=int(y)
z=0
a=[]
while(z<x):
    a.append(list(map(int,input().split())))
    z+=1
def above(a,i,j):
    return a[i-1][j]
def below(a,i,j):
    return a[i+1][j]
def right(a,i,j):
    return a[i][j+1]
def left(a,i,j):
    return a[i][j-1]
def center(a,i,j):
    return a[i][j]
mx=-1
m=n=o=p=1
value=0
for m in range(1,x-1):
    for n in range(1,y-1):
        for o in range(1,x-1):
            for p in range(1,y-1):
                if(not((o>m-2 and o<m+2) and (p>n-2 and p<n+2))):
                    value=(above(a,m,n)*above(a,o,p))+(below(a,m,n)*below(a,o,p))+(right(a,m,n)*right(a,o,p))+(center(a,m,n)*center(a,o,p))+(left(a,m,n)*left(a,o,p))
                    if(value>mx):
                        mx=value
print(mx)

