a=list(input())
if((int(a[0])+int(a[1]))%2==0):
    b=ord(a[2])
    if(b!=65 and b!=69 and b!=73 and b!=79 and b!=85 and b!=89):
        if((int(a[3])+int(a[4]))%2==0):
            if((int(a[4])+int(a[5]))%2==0):
                if((int(a[7])+int(a[8]))%2==0):
                    print("valid")
                else:
                    print("invalid")
            else:
                print("invalid")
        else:
            print("invalid")
    else:
        print("invalid")                    
else:
    print("invalid")
            
