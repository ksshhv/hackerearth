n = int(input())
for i in range(n):
    str1, str2 = input().split(' ')
    if sorted(str1) == sorted(str2):
        print("YES")
    else:
        print("NO")
