from turtle import *
import math

t = Turtle()

#user inputs color
#color=input("Enter Color!")
sides=input('How many sides?')
sides=int(sides)
length=input('How long should each side be?')
length=int(length)


t.penup()
# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)




#Draws any shape with user input of color and sides
t.pendown()
t.pencolor("blue")

for y in range(0,sides):
    z=1
    for x in range(0,sides+1):
        t.right(360/sides)
        t.speed(1000)
        t.forward(length)
        z=z+1
    t.right(((360/sides)*2)*z)


#for x in range(0,sides):
#    t.right(360/sides)
#    t.speed(1000)
#    t.forward(length)



# Close window on click.
exitonclick()
