def checkPalindrome(num):
#Implement Your Code Here
	rev = 0
	temp = num
	while num>0:
		r = num%10
		rev = (rev*10)+r
		num = num//10
	if temp == rev:
		return True
	else:
		return False
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')