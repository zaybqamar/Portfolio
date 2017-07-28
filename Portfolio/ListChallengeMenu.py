from random import *


#Create the lists of food you want to choose from.
appetizer_list = ["Caesar salad", "French onion soup", "garden salad", "tomato soup", "fries"]
maincourse_list = ["cheeseburger", "grilled chicken", "steak", "spaghetti", "salmon"]
dessert_list = ["chocolate cake", "brownie sundae", "strawberry shortcake", "fruit platter"]

#Generates a random meal.
x = randint(0, len(appetizer_list)-1)
y = randint(0, len(maincourse_list)-1)
z = randint(0, len(dessert_list)-1)
print("You ordered " + appetizer_list[x] + ", " + maincourse_list[y] + ", and " + dessert_list[z] + ".")
