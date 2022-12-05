def check_armstrong(n,l):
    sum = 0
    for each in n:
        sum = sum+(int(each)**l)
    if str(sum) == n:
        return True
    return False

n = input()
l = len(n)
if(check_armstrong(n,l)):
    print('true')
else:
    print('false')