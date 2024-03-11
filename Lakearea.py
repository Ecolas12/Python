#Emmanuel Colas - COP2500
#Lake area, use this program to calculate the area of Lake Knightrola

radius=int(input("What is the radius of the lake in meters?",))
#Radius of the lake should be an integer.
area= (3.141* radius**2)/2
#I entered 3.141 instead of just the pi value to keep the digits
#behind the decimal a lot smaller. When the user puts in the value,
#it will be calculated below with the correct unit.
print("The area of the lake is", area,"m^2")
