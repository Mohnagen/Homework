A = input().split()
b=1
for i in range(len(A)):
    b*=int(A[i])
print(b**(1/len(A)))