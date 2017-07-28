#Name: Mallory Grider
#Modified by: Zayba Qamar
#Date: July 27, 2017
"""Purpose: starter code for Caesar Shift Cipher program. The program both
	encrypts and decrypts plaintext."""
"""History:
	The caesar cipher is a symmetric key cipher that operates on the premise that
you rotate the alphabet a set number of characters creating a key. For
instance:
    A == Z
    B == A
    C == B
    ...
    Z == Y

QUICK CODE NOTE:
		YOU WILL NEED THE FOLLOWING BUILT-IN FUNCTIONS:
			1. ord(): returns the ASCII value of a character
			2. chr(): takes in an ASCII value and returns the character
			3. isalpha(): detects if input is a character in the alphabet
			4. find(): """


def encode(plaintext, shift_num):

	CipherText = ""
	OrdValue = 0
	RecycleValue = 0
	#Your code here
	for letter in plaintext:
		if ord(letter) + shift_num >= 97 and ord(letter) + shift_num <= 122:
			OrdValue = ord(letter) + shift_num
			CipherText += chr(OrdValue)
		elif ord(letter) + shift_num > 122:
			RecycleValue = (ord(letter) + shift_num) - 122
			OrdValue = 97 + RecycleValue
			CipherText += chr(OrdValue)
		else:
			print("else")


	print("Your ciphertext is: " + CipherText)
#	print(cipherText)

#Brute force method; checks against every possible shift (does not have access to a key)
def decode(ciphertext):
	print("Your plaintext is one of the following:")
	PlainText = ""
	OrdValue = 0
	shift_num = 1
	for x in range(0, 25):
		for letter in ciphertext:
			OrdValue = ord(letter) - shift_num
			PlainText += chr(OrdValue)
			print(PlainText)
			PlainText = ""
		shift_num += 1


	#Your code

user_input = str(input("Would you like to encode or decode a message?"))
plaintext = ""
shift_num = 0

if (user_input == "encode"):
	plaintext = input("What is your message?")
	shift_num = int(input("What would you like to shift the message by?"))
	encode(plaintext, shift_num)
elif (user_input == "decode"):
	ciphertext = input("What is your ciphertext?")
	decode(ciphertext)
else:
	print("Please input 'encode' or 'decode'"
