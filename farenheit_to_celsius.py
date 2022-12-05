s = int(input())
e = int(input())
w = int(input())

while s<=e:
    print(s, end=" ")
    print(int((s-32)*5/9))
    s+=w