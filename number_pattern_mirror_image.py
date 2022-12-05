'''
1    1
12  21
123321
'''

n = int(input())

i = 1
while i<=n:
    j = 1
    while j<=i:
        print(j, end='')
        j = j+1
    s = 1
    while s<=n-i:
        print(' ', end='')
        s = s+1
    s = 1
    while s<=n-i:
        print(' ', end='')
        s = s+1
    j = i
    while j>=1:
        print(j, end='')
        j = j-1
    print()
    i = i+1