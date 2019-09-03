x=int(input())
l=list(map(int,input().split()))
m = [0]*100000

for i in range(0,x):
    m[l[i]]
    m[l[i]]+=1

a=int(input())
while(a):
    b=int(input())
    if(m[b]>0):
        print(m[b])
    else:
        print("NOT PRESENT")
    a-=1
