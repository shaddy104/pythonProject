'''
A
BB
CCC
'''

n = int(input())
i=1
while i<=n:
    a = 65
    j=1
    while j<=i:
        print(chr((a+i)-1), end='')
        j=j+1
    print()
    i=i+1