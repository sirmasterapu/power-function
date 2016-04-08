
# def power(base, exponent):
# 
# 	""" Will raise the base to the exponent """
# 
# 	count = 0
# 	startingInteger = 1
# 			
# 	while count < exponent:
# 		count += 1
# 		startingInteger = startingInteger * base
# 		
# 	return startingInteger	
# 
# 
# def float_input(prompt): 
# 	"""Accepts a prompt for the user as a string. Returns answer as a float. Allows user 
# 	to try again."""
# 	
# 	number = raw_input(prompt) 
# 	notYetConverted = True
# 	
# 	while notYetConverted:
# 	
# 		try:
# 			number= float(number)
# 			
# 		except ValueError:
# 			number = raw_input("Sorry, that's not a number.Try again: ")
# 			
# 		else:
# 			notYetConverted = False
# 	return number 
# 	
# 		
# #######Calling Function#######
# userBase = float_input("Input the base of the number: ")
# userExponent = float_input("Input the exponent, greater than 0: ")
# endResult = power(userBase, userExponent)
# print("{} to the power of {} is {}.".format(userBase, userExponent, endResult))
# 		
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