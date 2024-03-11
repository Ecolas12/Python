#Emmanuel Colas - COP2500
#Monstermap.py - Creates a map based on the inputs given by the user in a 10x8 grid. 


#This function is called the Turtle position function. This function will be what is responsible for moving the
#turtle to the correct spot and the desired 10x8 grid. The function will draw a circle with the desired radius, pick up the
#pen, dropped it, and repeated. The function's parameters will be the horizontal/vertical multipliers and the constant that
#the user will input. it wil crash if the user doesnt put in a number. 
def turtle_position(duh_turtle, hori_m, verti_m, constant):
    x_coordinate =0
    while x_coordinate<10:
        x_coordinate = x_coordinate +1
        for y_coordinate in range(0,8):
            my_turtle.penup()
            my_turtle.goto(25*x_coordinate,-25 * y_coordinate)
            my_turtle.pendown()
            my_turtle.fillcolor("red")
            my_turtle.begin_fill()
            my_turtle.circle((hori_m * x_coordinate)+(verti_m* y_coordinate)+constant)
            my_turtle.end_fill()



#User interface that will ask for the desired values. 
print("Put in a whole number or in decimal form")
h_value=float(input("Horizontal Multiplier Value:",))
v_value=float(input("Vertical Multiplier Value:",))
constant= float(input("Constant Value:",))
            

#Turtle gets imported here so that it loads after it gets all of it
#parameters. 
import turtle
my_screen = turtle.getscreen()
my_turtle = turtle.Turtle()

turtle_position(my_turtle,h_value, v_value, constant)
