a=int(input())
while(a):
    green,purple=input().split()
    green=int(green)
    purple=int(purple)
    a=a-1
    first=0
    second=0
    b=int(input())
    #y=[['0','0'],['0','0'],['0','0'],['0','0'],['0','0'],['0','0'],['0','0'],['0','0'],['0','0'],['0','0']]
    while(b):
        x=list(map(str,input().split()))
        b=b-1
        first=first+int(x[0])
        second=second+int(x[1])
    print(min(green,purple)*max(first,second)+max(green,purple)*min(first,second))

