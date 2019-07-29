x=int(input())
while x>0 :
    p=list(input())
    s=list(input())
    dict={}
    for l in s:
        dict[l] = p.index(l)
    x=x-1
    print(dict)
    dict1={}
    l=list(sorted(dict.items(), key = 
             lambda kv:(kv[1], kv[0])))
    print(l)
    l1=[]
    for a in l:
        l1.append(a[0])
    print(l1)
    print("".join(map(str,l1)))
