#Emmanuel Colas - COP2500
#project.py - Fianl project. This program is like a little pokemon battle for the knightrolla competition.

#Problem: You are a young monster collector and you have enter a tournamnet to battle other monsters. But becoming a champ isnt easy so
#your coach wants to test your abttle strategy before you enter the tournament. This prgram will simulate a pokemon battle with your monster and
#a monster for the program. They will fight with 2 commands that range in damage. When either of their health reaches zero the program will ask if you want to
#battle again. 



import math
import random
#These two disctionaries are the monsters that will be fighting in the program. Knighty will be the user's monster and spidermon will be the program's monster.
#I gave them health and moves that the user/ program can call and inflict damage. 
Knighty = {
    "Name": "Knighty",
    "Health": 80.0,
    "Attack": "Sword Slash",
    "Special": "Charge On",
    }

Spidermon = {
    "Name": "Spidermon",
    "Health": 65.0,
    "Attack": "Web Shot",
    "Special": "Venom",
    }


#This is the round_fight function. This function will be simulating the battle. Depending on the what the user calls, it will use a random range to decide how much damage it will do
#to the spidermon. It will also randomly use it's 2 moves to inflict damge to you monster Knighty. The function accepts 2 monsters to fight. You have to put their names in the function
#and it will draw the stats from the dictionary. It returns the players health to determine if you won the match or was defeated.The function will crash if you dont put in a valid command.
def round_fight(hero,villain):
    name_hero = hero["Name"]
    health_hero = hero["Health"]
    attack_hero = hero["Attack"]
    special_hero = hero["Special"]
    damage_hero = 0
    sp_damage_hero = 0

    name_villain = villain["Name"]
    health_villain = villain["Health"]
    attack_villain = villain["Attack"]
    special_villain = villain["Special"]
    damage_villain = 0
    sp_damage_villain = 0
    
    print("(Tell",name_hero,"to Attack or say Special for a chance at more damage!)")
    
    while health_villain >= 0 and health_hero >= 0:
        damage_hero = random.randint(12, 20)
        sp_damage_hero = random.randint(3, 25)
        damage_villain = random.randint(4,15)
        sp_damage_villain = random.randint(7, 30)
        
        attack=input("Attack or Special?",)
        attack= attack.title()
        if attack == "Attack" or attack == "A":
            print(name_hero,"used",attack_hero,"and did",damage_hero,"damage!")
            health_villain = health_villain - damage_hero
        if attack == "Special" or attack == "S":
            print(name_hero,"used",special_hero,"and did",sp_damage_hero,"damage!")
            health_villain = health_villain - sp_damage_hero

            
        cpu_attack = random.randint(1,21)
        if cpu_attack >= 12:
            print(name_villain,"used",attack_villain,"and did",damage_villain,"damage!")
            health_hero = health_hero - damage_villain
        if cpu_attack <= 11:
            print(name_villain ,"used",special_villain,"and did",sp_damage_villain,"damage!")
            health_hero = health_hero - sp_damage_villain

        print(name_hero,"Health:", health_hero)
        print(name_villain,"Health:", health_villain)
        
    return health_hero
    
#Dialogue for the beginning of the program.          
print("Coach: You need to practice for the Big Knightrola Finals!")
print("Coach: You and your monster Knighty will fight against me and my Spidermon")


#The main function that runs the program. This will start the battle and continue the story depending on a win or lost. It also gives you a chance to battle again.
#It doesn't take parameters. It will run as long as round_fight goes to completion. 
def main():
    continues = round_fight(Knighty,Spidermon)
    if continues <=0:
        print("You're never gonna win like this!")
    else:
        print("Coach: GAH! I can't belive I lost! Hmph. You might have a chance of winning.")

    rerun =input("Wanna start over?Y or N:",)
    if rerun == "Y" or rerun == "y":
        main()


main()


    

