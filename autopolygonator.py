#Emmanuel Colas - COP 2500
#autopolygonator.py - This will allow you to draw a polygon
#just from a user imput of how many sides and perimeter of the polygon.

import turtle

#The user will put the parameters of the polygon
numsides = int(input("How many sides does the polygon have?", ))
perimeter = float(input("What's the perimeter?", ))

#Equations to deteremine the angle the turtle will turn and the length of each side
#of the polygon
angle= 360/ numsides
length = (perimeter / numsides)

#This function will tell python what each parameter is doing to draw the polygon.

def drawpolygon(theturtle, x, y, angle, length):
    #Gets the turtle to starting position
    theturtle.penup()
    theturtle.goto(x,y)
    theturtle.pendown()

    #Start drawing polygon. The range we put as numsides so that this cycle will repeat
    #for the number of sides that this polygon has. 
    for i in range(numsides):
        theturtle.forward(length)
        theturtle.left(angle)
       

my_screen = turtle.getscreen()
my_turtle = turtle.Turtle()
my_turtle.pensize (3)

#This string is using the angle and length that were determine earlier and will send it
#to the drawpolygon function. This is where the user input will affect the polygon drawing. 
drawpolygon(my_turtle,-0,-200,angle, length)
