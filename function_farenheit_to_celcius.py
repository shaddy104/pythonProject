def printTable(start,end,step):
	for i in range(start,end,step):
		print(i,end = '\t')
		farenheit2celsius(i)

def farenheit2celsius(n):
	print(int((5/9)*(n-32)))
	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)