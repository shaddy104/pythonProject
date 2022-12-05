'''
     1
    232
   34543
  4567654
 567898765
'''

n = int (input())
i = 1
while i<=n:
    s = 1
    # spaces
    while s<=n-i:
        print(' ', end = '')
        s = s+1
    j = 1
    x=i
    #patterns
    while j<=i:
        print(x, end = '')
        j = j+1
        x = x+1
    p = i-1
    x = x-1
    while p>=1:
        print(x-1,end='')
        p=p-1
        x = x-1
    print()
    i = i+1