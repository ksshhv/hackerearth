import math
x=int(input())
while(x):
    y=int(input())
    output=0
    z=1
    while(z<math.sqrt(y)):
        if(y%z==0):
            output+=2
        z+=1
    if(z==math.sqrt(y)):
        output+=1
    print(output)
    x-=1
