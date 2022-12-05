def checkPalindrome(num):
	n = num
	rev = 0
	while n>0:
		r = n%10
		rev = rev * 10 + r
		n = n//10
	if num == rev:
		return True
	return False
		
num = int(input())
isPalindrome = checkPalindrome(num)
if(isPalindrome):
	print('true')
else:
	print('false')