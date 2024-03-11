#Emmanuel Colas - COP 2500
#Quadplotter - Ask for the coefficient in a quadratic equation and plots the points.


#This is the calculate quad function used to calculate my y values. Each parameter is used
#used to be plugged into the equation when called on then gives you a y-value.
def calculate_quad(xx,aa,bb,cc):
    y = aa * xx**2 + bb * xx + cc
    return y


#This is my print_coordinates function. This function will take the return from
#calculate_quad function a tell python to print out my words and values.
def print_coordinates(xxx,aaa,bbb,ccc):
    yyy = calculate_quad(xxx,aaa,bbb,ccc)
    print("At x =",xxx, ", y =",yyy)



# The main function is what takes the user's input and sends them multiple functions to
#calculate values. This function has my x_values that were desired and will use
#conditional to stay in range. 
def main():
    a_value = float(input("Enter the a coeffiecient: ", ))
    b_value = float(input("enter the b coeffiecient: ", ))
    c_value = float(input("Enter the c coeffiecient: ", ))
    print(f"Parabola y = {a_value} x^2 + {b_value} x + {c_value}")
    for x in range (0,10):
        print_coordinates(x,a_value,b_value,c_value)

    x = 10
    while x < 100000000:
        print_coordinates(x,a_value,b_value,c_value)
        x= x*10

main()









