#importing the tutrle library
import turtle

#creating a turtle
myturtle = turtle.Pen()

#set turtle speed, default speed is 3
myturtle.speed(20)
myturtle.color("red", "orange")

#declare values for the loop, j for how many circles and step for the size of the first circle
j = 0
step = 2

myturtle.begin_fill()

while j < 60:
    i = 0
    #draw a circle
    while i < 18:
        myturtle.forward(step)
        myturtle.left(20)
        i += 1

    #turns the turtle 20 degrees to the left
    myturtle.left(20)
    #increases the step of the next circle by .5
    step += .5
    j += 1

myturtle.end_fill()
turtle.exitonclick()