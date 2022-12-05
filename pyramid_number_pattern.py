'''
   1
  212
 32123
4321234
'''

n = int(input())
i = 1
while i<=n:
    s = 1
    while s<=n-i:
        print(' ',end='')
        s = s+1
    j = 1
    p = s-1
    while j<=i:
        print(n-p,end='')
        j = j+1
        p = p+1
    j = 2
    while j<=i:
        print(j,end='')
        j = j+1
    i = i+1
    print()