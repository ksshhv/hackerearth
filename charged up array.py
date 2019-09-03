T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    x = 1
    k=N
    while(k):
        x=x*2
        k-=1
    x=x//2
    #print(x)
    for _ in range(N):
        if(A[_]<x):
            A[_]=0
    #print(A)
    sum=0
    for _ in range(N):
        sum+=A[_]
    print(sum%1000000007)
