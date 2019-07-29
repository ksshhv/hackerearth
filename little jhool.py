x=input()
y=0
a=0
b=0
c0=0
c1=0
while(y<len(x)):
    if(x[y]=="0"):
        c0=c0+1
        if(c0==6):
            print("Sorry, sorry!")
            a=1
            break
        c1=0
    if(x[y]=="1"):
        c1=c1+1
        if(c1==6):
            print("Sorry, sorry!")
            b=1
            break
        c0=0
    y=y+1
if(a==0 and b==0):
    print("Good luck!")
