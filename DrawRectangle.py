#importing the tutrle library
import turtle

#creating a turtle
myturtle = turtle.Pen()

#set turtle speed, default speed is 3
myturtle.speed(5)
#set color of turtle, first input value for lines second input value for filling
myturtle.color("red", "yellow")

#start filling
myturtle.begin_fill()

#draw line 100 forward 100 pixel
myturtle.forward(100)
#turns the turtles head to the left of 90 degrees. note: turtle head start with 0 degrees which is looking to the right
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)
myturtle.forward(100)
myturtle.left(90)

#stop filling
myturtle.end_fill()

turtle.exitonclick()