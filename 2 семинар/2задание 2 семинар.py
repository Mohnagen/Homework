F=input().strip()
n=int(input())
a=len(F) // n
x=''
for i in range(0, len(F), n):
    x+=F[i: i + n][::-1]
print(x)