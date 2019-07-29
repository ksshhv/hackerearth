y=int(input())
c=0
while(y):
    r,x=input().split()
    if((100*int(x))>=(2*(22/7)*int(r))):
        c+=1
    y-=1
print(c)
