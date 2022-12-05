'''
   1 
  12
 123
1234
'''

n = int(input())
i=1
while i<=n:
    space = 1
    while space<=n-i:
        print(' ',end='')
        space = space+1
    j =1
    while j<=i:
        print(j, end='')
        j=j+1
    i=i+1
    print()