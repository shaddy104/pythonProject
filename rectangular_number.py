'''
4444444
4333334
4322234
4321234
4322234
4333334  
4444444
'''

n = int(input())
i = n
while i>=1:
    
    s = 1
    v = n
    while s<=n-i:
        print(v, end='')
        s = s+1
        v = v-1
    j = 1
    while j<=i:
        print(i, end="")
        j = j+1
    j = 1
    while j<i:
        print(i, end="")
        j = j+1
    v = i+1
    s = 1
    while s<=n-i:
        print(v, end='')
        s = s+1
        v = v+1
    i = i-1
    print()

i = n
while i>1:
    j = 1
    v = n-j+1
    while j<i:
        print(v, end="")
        j = j+1
        v = v-1
    
    s = 1
    while s<=n-i:
        print(v+1, end='')
        s = s+1
    s = 1
    #v = n
    while s<=n-i+1:
        print(v+1, end='')
        s = s+1
        
    j = 1
    #v = n-j-1
    while j<i:
        print(v+1, end="")
        j = j+1
        v = v+1
    i = i-1
    print()