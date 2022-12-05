n = input()
even = 0
odd = 0
for x in n:
    if int(x)%2 == 0:
        even += int(x)
    else:
        odd += int(x)
print(even,odd)