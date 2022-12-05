'''
123456
 23456
  3456
   456
    56
     6
    56
   456
  3456
 23456
123456
'''

n = int(input())
for i in range(n,0,-1):
    for s in range(1,n-i+1):
        print(' ', end='')
    for j in range(1,i+1):
        print(n-i+j,end='')
    print()
for i in range(2, n+1):
    for s in range(1,n-i+1):
        print(' ', end='')
    for j in range(1,i+1):
        print(n-i+j, end='')
    print()
