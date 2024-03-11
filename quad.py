#Emmanuel Colas - COP 2500
#Quad.py - This program will give you the roots for a quadratic equation. 

import math
print("Answers must be a number")
a = float(input("What is the a coefficient?", ))
b = float(input("What is the b coefficient?", ))
c = float(input("What is the c coefficient?", ))


determinate = (b**2 - 4*a*c)

#The b-minus is to find the root where you minus determinate from b.
#Has the abc parameter to plug into the equation to give you back the
#the final answer "d". Thanks to the if statement, this will only activate if the
#condition is met.
def b_minus(a,b,c):
    d = (-b - math.sqrt(determinate))/(2 * a)
    print (d)
    return d

#The b_plus function is to find the root that is a results of determinate added to b.
#Has the abc parameter and they plug into the equation to give a return value "d".
# Thamks to the if statement this will only activate if the condition is met. 
def b_plus(a,b,c):
    d = (-b + math.sqrt(determinate))/(2 * a)
    print (d)
    return d


#The root number function will tell us how many roots we will have based
# on the a,b,c parameters. The abc parameters an plugged into the equation
#to get the determinate. As long as the user puts in a numbers and not a letter,
#everything should be fine.

def root_number (a,b,c):
    determinate = (b**2 - 4*a*c)
    if determinate < 0:
        print("This formula has complex roots")
    elif determinate ==0:
        b_minus(a,b,c)
        print("You have one root")
    elif determinate > 0:
        b_minus(a,b,c)
        b_plus(a,b,c)
        print("You have 2 roots")
    else:
        print("Invalid entry")
    return determinate

root_number(a,b,c)
    
    

