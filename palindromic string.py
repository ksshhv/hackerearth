x=input()
if(len(x)%2==1):
    y=int(len(x)/2)
    z=y
    while(z>=0):
        if(x[y-z]!=x[y+z]):
            print("NO")
            break
        else:
            z=z-1
    print("YES")
    
if(len(x)%2==0):
    y=int(len(x)/2)-1
    z=y
    while(z>=0):
        if(x[y-z]!=x[y+z+1]):
            print("NO")
            break
        else:
            z=z-1
    print("YES")
            
        
    
    

        
    
    
