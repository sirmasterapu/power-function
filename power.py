from powerFunctions import float_input
from powerFunctions import int_input
from powerFunctions import power
		
#######Calling Function#######
print("5 to the power of 0 is {}".format(power(5,0)))
print("-5 to the power of 2 is {}".format(power(-5,2)))
print("0 to the power of 10 is {}".format(power(0,10)))

userBase = float_input("Input the base of the number: ")
userExponent = int_input("Input the exponent, greater than 0: ")
endResult = power(userBase, userExponent)
print("{} to the power of {} is {}.".format(userBase, userExponent, endResult))
		