x=int(input())
y=input()
z=1
flag=0
while(z<x):
    if(y[z]=="H" and y[z-1]=="H"):
        print("NO")
        flag=1
        break
    z+=1
k=0
if(flag==0):
    print("YES")
    while(k<x):
        if(y[k]=="H"):
            print("H",end="")
        else:
            print("B",end="")
        k+=1

        
