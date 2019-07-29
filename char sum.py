x=list(input())
y=0
z=0
while(y<len(x)):
    z=z+(ord(x[y])-96)
    y+=1
print(z)
