#Emmanuel Colas - COP 2500
#Lineplotter.py - This program will give you the y value for set x values.
#The program will ask the user for the slope and intercept and it will calculate
#the y value. 


#This is where the program will ask for the user input. Had to change to float
#or else the program would give wrong calculations. Printed out the slope and
#intercept values as well.

slope = float(input("What is the slope of this line?", ))
intercept = float(input("What would you like the intercept to be?", ))

print("Slope:",slope)
print("Intercept:",intercept)
print("Line y =",slope,"x","+",intercept)

# Made x = -1 to start the process at zero. The "while" function below will add
#1 to x everytime the loop goes around. Then end when it gets to the number 10. 
x = -1

while x in range(-1,10):
    x = x + 1
    y = (slope * x)+ intercept
    print("At x =", x, "y =", y) 

#Made another "while" function so that I can cover the second set of x value.
#This time i did x times 10 to get the desired values. 

while x in range(10,100000):
    x = x * 10
    y = (slope * x)+ intercept
    print("At x =", x, "y =", y) 

