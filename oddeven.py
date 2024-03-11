#Emmanuel Colas - COP 2500
#OddEven.py - Lets play a game. Program will pick a odd or even number.
#User must guess it right or they lose.
import random

print("I'm thinking of a number between 1 and 256.")
user_answer=input("Can you guess if its odd or even?",)

program_number= random.randint(1,256)
print(program_number)

#The code below is a collection of if/elif statements for a combo of
#resonses. The code has an appropriate response for a correct with a
#corret reponse and vice versa. The else at the bottom of the code is
#for when they point an answer that isnt odd or even. 

if program_number%2 == 0 and user_answer == "even":
    print("Yay! You got it right!")
    
elif program_number%2 == 0 and user_answer == "odd":
    print("Sorry, It was even")
    
elif program_number%2 != 0 and user_answer == "odd":
    print("Yay! You got it right!")
    
elif program_number%2 != 0 and user_answer == "even":
    print("Sorry, It was odd")
    
else: print("Invalid Entry")

