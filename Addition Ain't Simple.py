a=int(input())
while(a):
    x=input()
    y=x[::-1]
    z=0
    while(z<len(x)):
        c=ord(x[z])+ord(y[z])-192
        if(c>26 and c<53):
            c=c-26
        print(chr(c+96),end='')
        z+=1
    print()
    a-=1
