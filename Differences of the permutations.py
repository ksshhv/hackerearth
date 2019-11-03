import math
t=int(input())
while(t):
    n=int(input())
    l=n*n-(n*(n+1)//2)
    print(int(math.factorial(n)*l))
    t-=1
