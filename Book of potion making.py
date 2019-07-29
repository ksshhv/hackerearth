x=list(input())
if(len(x)==10):
    y=0
    z=0
    while(y<10):
        z=z+(y+1)*(int(x[y]))
        y+=1
    if(z%11==0):
        print("Legal ISBN")
    else:
        print("Illegal ISBN")
else:
    print("Illegal ISBN")
