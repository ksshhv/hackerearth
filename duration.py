x=int(input())
while(x>0):
    a,b,c,d=input().split()
    e=((int(c)*60+int(d))-(int(a)*60+int(b)))
    print(str(int(e/60))+" "+str(int(e%60)))
    x-=1
    
