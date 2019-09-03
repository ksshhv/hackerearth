a,b=input().split()
a=int(a)
b=int(b)
x=list(map(int,input().split()))
g=0
count=0
m=[0]*100000
for i in range(0,a):
    m[x[i]]
    m[x[i]]+=1
twice_count = 0
for i in range(0,a):
    twice_count += m[b-x[i]]
    if(b-x[i]==x[i]):
        twice_count-=1
count=twice_count/2
print(int(count))
print(m)
