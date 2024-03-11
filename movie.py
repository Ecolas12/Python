#Emmanuel Colas - COP2500
#movies.py - Program to determine the ticet pricing of guests.

#Added a little header letting the user know about the deal going on with
# over 25 people. The value has to be an integer so I added that command.
#Added spaces behind the second question to get the inputs align on screen.

print("*For parties 25 or more members, group rates are 7.25 per person*")
VIP=int(input("How many Small Monster Collectors are in your party?",))
Admin=int(input("How many are general admission?                     ",))

#I added a total value that will count the inputs from the above questions.
#From there I added the math equations to calculate a price.
#I used an "if" command for when the user's inputs equal to more than 25
#they are able to activate the deal. 
total= VIP + Admin
Price= (9.50* VIP) + (12* Admin)
if total >= 25:
    Price= (7.25* total)

print("Total Price is $",Price)
