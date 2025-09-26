with open('C:/Users/Пользователь/Desktop/asd/input.txt', 'r') as f:
    l=f.readlines()
    n=list(map(int, l[0].split()))
    x=l[1].strip()
    if x == '+':
        r=0
        for i in range(len(n)):
            r+=n[i]
    elif x == '-':
        r=0
        for i in range(len(n)):
            r-=n[i]
    elif x == '*':
        r=1
        for i in range(len(n)):
            r*=n[i]
with open('C:/Users/Пользователь/Desktop/asd/output.txt', 'w') as f:
    f.write(str(r))