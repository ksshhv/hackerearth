d=int(input())

oc,of,od=map(int,input().split())
cs,cb,cm,cd=map(int,input().split())
online=0
classic=0

if d>of:
    online=oc+(d-of)*od
else:
    online=oc

classic=cb+(d//cs)*cm+d*cd

if(online<=classic):
    print("Online Taxi")
else:
    print("Classic Taxi")
