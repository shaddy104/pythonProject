def checkMember(n):
    a = 1
    b = 1
    for i in range(0,n+1):
        if n == 0 or n == 1:
            return True
        c = a+b
        a = b
        b = c
        if(n == c):
            return True
    return False

n=int(input())
if(checkMember(n)):
    print("true")
else:
    print("false")