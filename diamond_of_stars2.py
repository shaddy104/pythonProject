'''
  *
 ***
*****
 ***
  *
'''

n = int(input())
for i in range(1,(n+1)//2):
    for s in range(((n+1)//2)-i):
        print(' ',end='')
    for j in range(1, i+1):
        print('*',end='')
    for t in range(i,1,-1):
        print('*',end='')
    print()
for i in range((n//2)+1,0,-1):
    for s in range(((n//2)+1)-i):
        print(' ',end='')
    for j in range(1, i+1):
        print('*',end='')
    for t in range(i,1,-1):
        print('*',end='')
    print()


'''

n=int(input())
n1=((n+1)/2)
i=1
while i<=n1:
    spcs=1
    while spcs<=(n1-i):
        print(" ",end="")
        spcs=spcs+1
    stars=1
    while stars<=(2*i-1):
        print("*",end="")
        stars=stars+1
    print()
    i=i+1
i=n-n1
while i>=1:
    spcs=1
    while spcs<=(n1-i):
        print(" ",end="")
        spcs=spcs+1
    stars=1
    while stars<=(2*i-1):
        print("*",end="")
        stars=stars+1
    print()
    i=i-1

'''