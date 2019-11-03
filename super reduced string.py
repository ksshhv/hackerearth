s=input()
k=0
out=[0]
while(k<len(s)):
    if(out[len(out)-1]==s[k]):
        out.pop()
    else:
        out.append(s[k])
    k+=1
u=1
if(len(out)==1):
    print("Empty String")
else:
    while(u<len(out)):
        print(out[u],end="")
        u+=1
    
    
