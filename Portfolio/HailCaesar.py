#Create function to encode from plaintext to ciphertext
def encode(plaintext, shift_num):
	#Create eventual string for output
	ciphertext = ""
	#Cycle through each letter
	for letter in plaintext:
		#If ciphertext letter is before z
		if ord(letter) + shift_num >= ord("a") and ord(letter) + shift_num <= ord("z"):
			OrdValue = ord(letter) + shift_num
			ciphertext += chr(OrdValue)
		#If ciphertext letter recycles through alphabet
		elif ord(letter) + shift_num > ord("z"):
			RecycleValue = (ord(letter) + shift_num) - ord("z")
			OrdValue = ord("a") + RecycleValue - 1
			ciphertext += chr(OrdValue)

	"""	if ord(letter) + shift_num > ord("z"):
			shift_num = (ord(letter) + shift_num) - ord("z")
		OrdValue = ord(letter) + shift_num
		ciphertext += chr(OrdValue)"""


	#Print ciphertext
	print("Your ciphertext is: " + ciphertext)


#Brute force method; checks against every possible shift (does not have access to a key)
#Create function to decode from ciphertext to plaintext
def decode(ciphertext):
	#Create variables and eventual string for output
	OrdValue = 0
	shift_num = 1
	#plaintext = ""
	print("Your plaintext is one of the following:")
	#Cycles through the 25 possibilities
	for x in range(0, 25):
		plaintext = ""
		#Cycles through each letter of plaintext
		for letter in ciphertext:
			#Applies to letters that shift within z through a
			if ord(letter) - shift_num >= ord("a"):
				OrdValue = ord(letter) - shift_num
				plaintext += chr(OrdValue)
			#Applies to letters that shift past a back through z
			elif ord(letter) - shift_num < ord("a"):
				#Calculates number needed to subtract from z one cycled through
				RecycleValue = ord("a") - 1 - (ord(letter) - shift_num)
				OrdValue = ord("z") - RecycleValue
				plaintext += chr(OrdValue)
		print(plaintext)
		#Increase shift number to account for all possibilities
		shift_num += 1

#Set loop variable
a = 1
#Create while loop to ultimately repeat if else is entered
while a > 0:
	#Ask for input and create initial string and variable
	user_input = str(input("Would you like to encode or decode a message?"))
	plaintext = ""
	shift_num = 0

	#Go down encode path
	if (user_input == "encode"):
		#Set loop variable
		b = 1
		#Create while loop to ultimately repeat if non alphabetical character is entered
		while b > 0:
			plaintext = input("What is your message?")
			#Check if plaintext contains only alphabet letters
			if plaintext.isalpha() == True:
				# Set loop variable
				c = 1
				#Create while loop to ultimately repeat if number greater than 25 is entered
				while c > 0:
					shift_num = int(input("What would you like to shift the message by?"))
					#Check if shift number is less than 27
					if shift_num <= 26:
						#Call encode function
						encode(plaintext, shift_num)
						#Ends shift while loop
						c = 0
					elif shift_num > 26:
						print("Please enter a number between 1 and 26.")
						c = 1
				#Ends entire while loop
				a = 0
				#Ends message while loop
				b = 0
			elif plaintext.isalpha() == False:
				print("Please enter English alphabet letters only.")

#Go down decode path
	elif (user_input == "decode"):
		b = 1
		while b > 0:
			ciphertext = input("What is your ciphertext?")
			if ciphertext.isalpha() == True:
				decode(ciphertext)
				#Ends entire while loop
				a = 0
				#Ends enter ciphertext while loop
				b = 0
			elif ciphertext.isalpha() == False:
				print("Please enter English alphabet letters only.")
	#User input was neither encode or decode
	else:
		print("Please input 'encode' or 'decode'")
