N=int(input())
a=input().split()
c=''.join(a[1:])
m=len(a) // 2 + 1
for i in range(len(a)):
    s=0
    for j in range(len(a)):
        if a[i]>=a[j]:
            s+=1
    if s == m:
        print(a[i])