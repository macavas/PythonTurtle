#importing the tutrle library
import turtle

#creating a turtle
myturtle = turtle.Pen()

#set turtle speed, default speed is 3
myturtle.speed(5)

#declare a counting value
i = 0

#start loop. note: need a loop with 36 repetition because our turtle turns 10 degrees to the left. so we need 360/10 to get a exact turn
while i < 36:
    #draw line 5pixels forwards
    myturtle.forward(5)
    #turn to the left 10 degrees
    myturtle.left(10)
    i += 1

turtle.exitonclick()