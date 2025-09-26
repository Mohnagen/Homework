n = input().split()
n[:-1:2],n[1::2] = n[1::2],n[:-1:2] 
print(n)