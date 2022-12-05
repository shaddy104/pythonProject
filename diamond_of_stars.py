'''
  *
 ***
*****
 ***
  *
'''

n = int(input())
i = 1
while i<=(n//2)+1:
    s = 1
    while s<=((n//2)+1)-i:
        print(' ',end='')
        s = s+1
    j = 1
    while j<=i:
        print('*',end='')
        j = j+1
    x = n-1
    p = i-1
    while p>=1:
        print('*', end = '')
        p = p-1
        x = x-1
    print()
    i = i+1
#i = (n//2) # 6//2 => 3
i = n - (n//2+1) # 6 - (6//2+1) => 2
while i>=1:
    s = 1
    while s<=((n//2)+1)-i:
        print(' ',end='')
        s = s+1
    j = 1
    while j<=i:
        print('*',end='')
        j = j+1
    x = n-1
    p = i-1
    while p>=1:
        print('*', end = '')
        p = p-1
        x = x-1
    print()
    i = i-1