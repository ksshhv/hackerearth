a=list(input())
x=0
y=0
b=0
while(b<len(a)):
    if(a[b]=="L"):
        x-=1
    if(a[b]=="R"):
        x+=1
    if(a[b]=="U"):
        y+=1
    if(a[b]=="D"):
        y-=1
    b=b+1
print(str(x)+" "+str(y))
