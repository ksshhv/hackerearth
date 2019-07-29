n,a,b=input().split()
c=list(map(str,input().split()))
k=0
m=0
while(m<int(n)):
    if(not (int(c[m])>=int(a) and int(c[m])<=int(b))):
        print("NO")
        k=k+1
        break
    m+=1
if(k==0):
    print("YES")
