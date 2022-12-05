'''
*
 * *
   * * *
     * * * *
   * * *
 * *
*
'''

n = int(input())
i = 1
x = 1
while x<=n//2+1:
    j = 1
    while j<=x-1:
        print(' ', end = '')
        j = j+1
    j = 1
    while j<=x:
        print('* ', end = '')
        j = j+1
    print()
    x = x+1
x = n//2
while x>=1:
    j = 1
    while j<=x-1:
        print(' ', end = '')
        j = j+1
    j = 1
    while j<=x:
        print('* ', end = '')
        j = j+1
    print()
    x = x-1
print()
i = i+1