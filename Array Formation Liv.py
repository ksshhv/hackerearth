x=int(input())
l=list(map(int,input().split()))
k=0
queue=[]
stack=[]
def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
while(k<x):
    if(isPrime(l[k])):
        queue.append(l[k])
    else:
        stack.append(l[k])
    k+=1
s=0
while(s<len(queue)):
    print(queue[s],end=" ")
    s+=1
t=len(stack)-1
print()
while(t>-1):
    print(stack[t],end=" ")
    t-=1
