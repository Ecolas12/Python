#Emmanuel Colas - COP 2500
#Vehicle - An outline of the monster collector vehicle.

import turtle
my_screen = turtle.getscreen()
my_turtle = turtle.Turtle()
my_turtle.pensize(3)

#Body for my vehicle.
#Going to be just a basic hull. increase the pensize to 3
#so that the outline will ne thicker.
my_turtle.penup()
my_turtle.goto(-300,0)
my_turtle. pendown()
my_turtle.forward(600)
my_turtle.left(45)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(45)
my_turtle.forward(600)
my_turtle.left(90)
my_turtle.forward(140)

#Floatation Device under the vehicle
#Suppose to be a big air sac that can slide on any surface.
#I just made a half circle on both ends and connected them.
#I picked different pen sizes for each peice of the vehicle.
my_turtle.pensize(8)
my_turtle.right(90)
my_turtle.circle(70,180)
my_turtle.forward(650)
my_turtle.circle(70,180)
my_turtle.forward(50)

#Rocket boosters on side
my_turtle.pensize(3)
my_turtle.penup()
my_turtle.goto(-375,55)
my_turtle.setheading(0)
my_turtle.pendown()
my_turtle.forward(150)
my_turtle.circle(25,180)
my_turtle.forward(150)
my_turtle.left(90)
my_turtle.forward(50)


#Windsheild
my_turtle.pensize(8)
my_turtle.penup()
my_turtle.goto(200,140)
my_turtle.setheading(135)
my_turtle.pendown()
my_turtle.forward(150)

#Propellor to gain altitude
my_turtle.pensize(3)
my_turtle.penup()
my_turtle.goto(-200,140)
my_turtle.setheading(90)
my_turtle.pendown()
my_turtle.goto(-200,320)
my_turtle.pensize(6)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.goto(-200,320)
my_turtle.setheading(0)
my_turtle.forward(100)


