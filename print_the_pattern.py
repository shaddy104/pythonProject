'''
 1    2   3    4   5
 11   12  13   14  15
 21   22  23   24  25
 16   17  18   19  20
 6    7    8   9   10
'''

n = int(input())
i = 1
x = 1
while i <= n:
    j = x
    while j < x+n:
        print(j,end=' ')
        j = j+1
    print()
    if i == (n+1)//2:
        if n%2 != 0:
            x = n*(n-2)+1
        else:
            x = n*(n-1)+1
    elif i > (n+1)//2:
        x = x-(2*n)
    else:
        x = x+(2*n)
    i = i+1