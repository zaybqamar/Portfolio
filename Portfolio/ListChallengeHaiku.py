from random import *

#Create the lists of lines you want to choose from.
five_syllables = ["Cars drive down the street", "I ran to the stream", "She smiled at her friend", "Leaves fall from the tree"]
seven_syllables = ["The butterfly flies away", "Little kids jump up and down", "I'll see you all tomorrow", "I left home at three o'clock"]

#Generates three random lines.
x = randint(0, len(five_syllables)-1)
y = randint(0, len(seven_syllables)-1)
z = randint(0, len(five_syllables)-1)

#String lines together
haiku = (five_syllables[x]) + "\n" + (seven_syllables[x]) + "\n" + (five_syllables[x])

print(haiku)
