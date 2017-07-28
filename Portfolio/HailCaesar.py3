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
The cipher is very insecure as when you find the offset you have found the
key. Running it through 26 variations will crack it easily. It also can be
cracked by letter frequencies.

The cipher was invented by Julius Caesar to encrypt military messages. Caesar used a
shift of 3.

It was secure most likely when Julius Caesar invented it but never again
(note that most of Julius Caesar's enemies were illerate).

QUICK CODE NOTE:
		YOU WILL NEED THE FOLLOWING BUILT-IN FUNCTIONS:
			1. ord(): returns the ASCII value of a character
			2. chr(): takes in an ASCII value and returns the character
			3. isalpha(): detects if input is a character in the alphabet
			4. find(): """

def encode(plaintext, shift_num):

	#Your code here





	print("Your ciphertext is: ")
	print(cipherText)

#Brute force method; checks against every possible shift (does not have access to a key)
def decode(ciphertext):

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
	print("Please input 'encode' or 'decode'")
