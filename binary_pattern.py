'''
1111
000
11
0
'''

n = int(input())
w = 0
for i in range(n,0,-1):
    for j in range(1,i+1):
        if i == n or i == n-w:
            print('1', end = '')
            continue
        else:
            print('0', end = '')
            continue
    if i == n or i == n-w:
        w = w+2
    print()