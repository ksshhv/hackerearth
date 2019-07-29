p=int(input())
l=float(input())
minutes=(p/6)*l
ah=minutes/2
am=(minutes%60)*6
a=abs(am-ah)
b=360-a
print("{:.2f}".format(round(min(a,b)),2),end="")
