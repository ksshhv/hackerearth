x=int(input())
a=[]
b=[]
while(x):
    y,z=input().split()
    if(y=="Coin"):
        a.append(z)
    if(y=="Note"):
        b.append(z)
    x-=1
h=len(a)
k=len(b)
l=0
m=0
print("Coins :")
while(l<h):
    print(a[l])
    l+=1
print("Notes :")
while(m<k):
    print(b[m])
    m+=1
    
