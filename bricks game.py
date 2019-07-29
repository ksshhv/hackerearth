x=int(input())
i=1
while(x>0):
    x=x-i
    if(x<1):
        print("Patlu")
        break
    x=x-2*i
    if(x<1):
        print("Motu")
        break
    i+=1

        
    
    
