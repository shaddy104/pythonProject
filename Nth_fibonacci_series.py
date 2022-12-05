n = int(input())
i = 1

while i<=n:
    if i == 1 or i==2:
        a=1
        b=1
    else:
        c = a+b
        a=b
        b=c
    i=i+1
print(b)