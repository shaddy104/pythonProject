'''
*000*000*
0*00*00*0
00*0*0*00
000***000
'''

n = int(input())
i = 1
while i<=n:
    j = 1
    while j<=i:
        if i == j:
            print('*', end='')
        else:
            print('0',end='')
        j = j+1
    s = 1
    while s<=n-i:
        print('0',end='')
        s = s+1
    print('*', end='')
    s = 1
    while s<=n-i:
        print('0',end='')
        s = s+1
    j = 1
    while j<=i:
        if j == 1:
            print('*', end='')
        else:
            print('0',end='')
        j = j+1
    print()
    i = i+1