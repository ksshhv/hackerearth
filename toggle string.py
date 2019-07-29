x=input()
y=0
z=""
while(y<len(x)):
    if(ord(x[y])>96 and ord(x[y])<123):
        z=z+str(chr(ord(x[y])-32))

    if(ord(x[y])>64 and ord(x[y])<91):
        z=z+str(chr(ord(x[y])+32))
    y=y+1
print(z)

    
