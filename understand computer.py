import math

def perfectsquare(number):
    root = math.sqrt(number)
    if int(root + 0.5) ** 2 == number:
        return number
    else:
        return 0
a=['0']
for i in range(10**12):
    a.append(i)
    if(perfectsquare(i)==i):
        a.append(i)
x=int(input())
while(x):
    y=int(input())
    print(a[y])
    x=x-1
        
