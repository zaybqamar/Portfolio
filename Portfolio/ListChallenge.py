from random import *


#Create the list of names you want to choose from.
name_list = ["Bob", "Sarah", "Zayba", "Alexa", "Joe", "Sally", "Henry"]

#Generates a random name.
x = randint(0, len(name_list)-1)
print(name_list[x])
