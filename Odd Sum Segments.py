x=int(input())
while(x):
	y,z=input().split()
	y=int(y)
	z=int(z)
	a=list(map(int,input().split()))
	b=0
	c=[]
	while(b<y):
		if(a[b]%2==1):
			c.append(b+1)
		b+=1
	if((len(c)>z and (len(c)-z)%2==0) or len(c)==z):
		k=0
		print("YES")
		while(k<z-1):
			print(c[k],end=" ")
			k+=1
		print(c[len(c)-1])
	else:
		print("NO")
	x-=1
