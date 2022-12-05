'''
E
DE
CDE
BCDE
ABCDE
'''

n = int(input())
i=1
while i<=n:
    j = 1
    asccii = 65
    while j<=i:
        print(chr((asccii+n)-i), end='')
        asccii = asccii+1
        j = j+1
    print()
    i=i+1