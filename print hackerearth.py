x=int(input())
y=input()
a=0
b=0
c=0
d=0
e=0
f=0
g=0
while(x):
    if(y[x-1]=="h"):
        a=a+1
        #2
    if(y[x-1]=="a"):
        b=b+1
        #2
    if(y[x-1]=="c"):
        c=c+1
    if(y[x-1]=="k"):
        d=d+1
    if(y[x-1]=="e"):
        e=e+1
        #2
    if(y[x-1]=="r"):
        f=f+1
        #2
    if(y[x-1]=="t"):
        g=g+1
    x=x-1
print(min(int(a/2),int(b/2),c,d,int(e/2),int(f/2),g))
