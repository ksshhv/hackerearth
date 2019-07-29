x=int(input())
while(x):
    y=input()
    y=y.lower()
    z=0
    count=0
    while(z<len(y)):
        if(y[z]=="a" or y[z]=="e" or y[z]=="i" or y[z]=="o" or y[z]=="u"):
            count+=(z+1)*(len(y)-z)
        z+=1
    print(count)
    x-=1
