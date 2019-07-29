x=list(input())
y=int(input())
a=0
b=""
while(a<len(x)):
    d=0
    if(int(ord(x[a]))>64 and int(ord(x[a]))<91):
        c=(int(ord(x[a])-65)+y)%26+65
        b=b+chr(c)
        d=1
    if(int(ord(x[a]))>96 and int(ord(x[a]))<123):
        c=(int(ord(x[a])-97)+y)%26+97
        b=b+chr(c)
        d=1
    if(int(ord(x[a]))>47 and int(ord(x[a]))<58):
        c=(int(ord(x[a])-48)+y)%10+48
        b=b+chr(c)
        d=1
    if(d==0):
        b=b+x[a]
    a+=1
print(b)
