#Emmanuel Colas - COP 2500
#Mathfun.py - This program will calculate the missing side or angle of a right triangle.

import math
#Calculate adjacent length function. Does what the names says and it will calculate a value for
#the adjacent side of a triangle. Calculate the adjacent length given hyp and adj angle using
#cos() * hyp. It will need the angle and hypotenuse for calculations and return the aadjacent
#length. There will be an error if the input values arent numbers.
def calculate_adjacent_length(ang,hyp):
    radian= ang*(3.14/180)
    adjacent =(math.cos(radian))*hyp
    return adjacent
#This is the print_adjacent length function. It will be called later when i need to
#print my results. The parameters are for the calculate_adjacent_length to use.
def print_adjacent_length(ang2,hyp2):
    adjacent = calculate_adjacent_length(ang,hyp)
    print ("The adjacent length is:",adjacent)
    
#The calculate_opposite_length function. Calculate the opposite length given the hypotenuse and
#the adjacent angle using sin() * hyp. The parameters are used for the calculations then it returns
#the opposite length value. Will cause error if the input values arent number.
def calculate_opposite_length(ang,hyp):
    radian= ang*(3.14/180)
    opposite = (math.sin(radian))*hyp
    return opposite
#Print adjacent length function. Is called to when I need to print the values of the other function.
#It will call the previous function and will print out the return value. Works as long as the
#other function works. 
def print_opposite_length(ang2,hyp2):
    opposite = calculate_opposite_length(ang,hyp)
    print("The opposite length is:",opposite)
    
#The calculate_adjacent_angle function is the first fuction that we use to find the angle. It
#calculate the adjacent angle given the hypotenuse and the opposite length using arcsin(opp/hyp).
#It will crash if it can't find the required numbers in the program.
def calculate_adjacent_angle(opp,hyp):
    adjacent_angle= (math.asin(opp/hyp))
    degrees = math.degrees(adjacent_angle)
    return degrees
#The print_adjacent_angle function is called later when I need to print my results. The parameters are given to the above function
#so that it can do the calculations and give it the value it needs to print. Will fail if the above function fails. 
def print_adjacent_angle(opp2,hyp2):
    angle=calculate_adjacent_angle(opp,hyp)
    print("The angle is:", angle)
    
#This is the second function to find the angle called calculate_adjacent_angle_2. (keep it simple). It will
#calculate the adjacent angle given the adjacent and opposite lengths using arctan(opp/adj). The parameters
#are from user inputs and will be used for calculations. It will go wrong if the user puts in a letteer
#instead of number.
def calculate_adjacent_angle_2(opp,adj):
    adjacent_angle_2= (math.atan(opp/adj))
    degrees = math.degrees(adjacent_angle_2)
    return degrees

#The last print function that is on the program. Called print_adjacent_function_2, this will fail if the above function fails. Just like the rest it will give the
#above function the paraters and print out the values when called. 
def print_adjacent_angle_2(opp2,adj2):
    degrees=calculate_adjacent_angle_2(opp,adj)
    print("The adjacent angle is:",degrees)
    

#The user input area. Will ask for the known sides and angle of the triangle. It can accept
#floats incase the triangle doesnt have only interger values. It will fail if the user doesnt
#put in a number value. 
print("TO find all side of a triangle and the adjacent angle,")
print("type in the known value when prompt and type in zero if the")
print("value is unknown.")
hyp=float(input("Hypotenuse:",))
opp=float(input("Opposite side:",))
adj=float(input("Adjacent side:",))
ang=float(input("Angle:",))


#This is where the conditional will find any unknown values(0), run calculation of the other values and then goo back
#around and fill in any missing numbers. Then it will print them all out with the n=ew calculations. If the user put in
#an alphabetical value it will crash. 
while hyp==0 or opp==0 or adj==0 or ang==0:
    if hyp==0:
        hyp= math.sqrt(opp**2 +adj**2)
    if opp==0:
        opp=calculate_opposite_length(ang,hyp)
        opp= math.sqrt(hyp**2-adj**2)
    if adj==0:
        adj=calculate_adjacent_length(ang,hyp)
    if ang==0:
        ang=calculate_adjacent_angle(opp,hyp)
        ang=calculate_adjacent_angle_2(opp,adj)

    print("The hypotenuse is:",hyp)
    print_adjacent_length(ang,hyp)
    print_opposite_length(ang,hyp)
    print_adjacent_angle(opp,hyp)


