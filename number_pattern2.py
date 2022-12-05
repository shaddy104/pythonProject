'''
1
11
202
3003
'''

n = int(input())
i=1
while i<=n:
    j=1
    while j<=i:
        if i==1 or i==2:
            print('1', end='')
        elif i==j or j==1:
            print(i-1, end='')
        else:
            print('0',end='')
        j=j+1
    print()
    i=i+1