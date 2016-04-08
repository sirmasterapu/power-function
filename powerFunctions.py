
def power(base, exponent):

	""" Will raise the base to the exponent """

	if exponent == 0:
		return 1
	else:
		output = base * power(base,exponent - 1)
	
	return output
	
		
	return startingInteger	


def float_input(prompt): 
	"""Accepts a prompt for the user as a string. Returns answer as a float. Allows user 
	to try again."""
	
	number = raw_input(prompt) 
	notYetConverted = True
	
	while notYetConverted:
	
		try:
			number= float(number)
			
		except ValueError:
			number = raw_input("Sorry, that's not a number.Try again: ")
			
		else:
			notYetConverted = False
	return number 
	
	
def int_input(prompt): 
	"""Accepts a prompt for the user as a string. Returns answer as a int. Allows user 
	to try again."""
	
	number = raw_input(prompt) 
	notYetConverted = True
	
	while notYetConverted:
	
		try:
			number= int(number)
			
		except ValueError:
			number = raw_input("Sorry, that's not a number.Try again: ")
			
		else:
			notYetConverted = False
	return number