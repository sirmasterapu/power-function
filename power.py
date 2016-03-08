
def power(base, exponent):
	count = 0
	
	while count < exponent:
	
		try:
			base = float(base)
			newBase = base * base
			
		except ValueError:
			print("not a number")
			
		count += 1

	return newBase
		




base = raw_input("Input the base of the number: ")
exponent = raw_input("Input the exponent, greater than 0: ")

output = power(base, exponent)
print(ouput)