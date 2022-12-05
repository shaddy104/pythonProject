flag = True
while flag:
    n = int(input())
    if n == 1:
        a = int(input())
        b = int(input())
        print(a+b)
    elif n == 2:
        a = int(input())
        b = int(input())
        print(a-b)
    elif n == 3:
        a = int(input())
        b = int(input())
        print(a*b)
    elif n == 4:
        a = int(input())
        b = int(input())
        print(a//b)
    elif n == 5:
        a = int(input())
        b = int(input())
        print(a%b)
    elif n == 6:
        flag = False
    else:
        print("Invalid Operation")