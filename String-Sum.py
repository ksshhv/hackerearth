x=input()
b=0
a=0
while(b<len(x)):
    a+=(ord(x[b])-96)
    b+=1
print(a)
