from math import sqrt
n=int(input())
ls=[int(x) for x in input().split()]
ls.insert(0,0)
ls1=ls.copy()
for i in range(1,n+1):
    ls1[i]+=ls1[i-1]
    sum=ls[n]
for i in range(1,n+1):
    x=int(sqrt(2*(n-i+1)))
    while((x*(x+1))/2 > n-i+1):
        x-=1
    x=int((x*(x+1))/2)
    if (ls1[i+x-1]-ls1[i-1])>sum:
        sum=ls1[i+x-1]-ls1[i-1]
print(sum)
