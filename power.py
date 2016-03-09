
def power():
	count = 0
	converted = False
	base = 1
	
	while converted == False:
		userBase = raw_input("Input the base of the number: ")
		userExponent = raw_input("Input the exponent, greater than 0: ")
		
		try:
			newBase = float(userBase)
			newExponent = int(userExponent)
			
		except ValueError:
				print("not a number. try again. ")
				
		
		else:
			converted = True
			
	while count < newExponent:
		count += 1
		base = base * newBase
		
	print(base)		

power()
		







