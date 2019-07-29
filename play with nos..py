a,b=input().split()
x=list(map(str,input().split()))
h=[]
for i in range(int(a)):
    g=int(i)
    y=0
    while(g>=0):
        y=y+int(x[g])
        g=g-1
    h.append(y)
while(int(b)>0):
    c,d=input().split()
    m=h[int(d)]-h[int(c)]
    m=int(m/(int(d)-int(c)+1))
    print(m)
