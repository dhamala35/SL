# 1b.
# Write a temperature converter python program, 
# which is menu driven. 
# Each such conversion logic should be 
# defined in separate functions. 
# The program should call the respective 
# function based on the user’s requirement. 
# The program should run as long as the user wishes so. 
# Provide an option to view the conversions stored 
# as list of tuples with attributes - 
# from unit value , to unit value sorted by 
# the user’s choice (from-value or to-value).

def FtoC(F):
	C = (5.0/9.0)*(F-32)
	return C

def CtoF(C):
	F = (9.0/5.0)*C + 32
	return F

def choice():
	print ("1. Fahrenheit to celcius.")
	print ("2. Celcius to Fahrenheit.")
	print ("3. Exit.")

def main():
	again = True
	while(again):
		choice = int(input("Enter a choice."))
		if choice == 1:
			F = float(input("Temperature in Fahrenheit?\n"))
			C = FtoC(F)
			print ("Temperature in Celcius: ", C)

		if choice == 2:
			C = float(input("Temperature in Celcius?\n"))
			F = CtoF(C)
			print ("Temperature in Fahrenheit: ", F)

		elif choice == 3:
			again = False
choice()
main()
