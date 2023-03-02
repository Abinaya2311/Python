def sumseries(n):
	sum = 0
	for i in range (0, n+1):
		sum+=pow(i,2)	
	return sum

n = int(input("Enter a number: "))
print("Sum of series of",n,"is: ", sumseries(n))
