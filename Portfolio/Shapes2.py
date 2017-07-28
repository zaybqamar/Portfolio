from turtle import *
import math

# Name your Turtle.
t = Turtle()

t.penup()
# Set Up your screen and starting position.
setup(500,300)
x_pos = 0
y_pos = 0
t.setposition(x_pos, y_pos)

### Write your code below:

#Draws a square
t.pendown()
for x in range(0,4):
    t.right(90)
    t.speed(1000)
    t.forward(50)

t.penup()
t.forward(100)
t.pendown()

#Draws a triangle
for x in range(0,3):
    t.right(120)
    t.speed(1000)
    t.forward(50)


# Close window on click.
exitonclick()
