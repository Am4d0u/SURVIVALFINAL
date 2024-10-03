from os import name
from tkinter import N
from typing import Self
from artwork import *

pegi()
survival()
name = input("What is your name? \n")

while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")

while int(len(name)) > 15:
    print("Characters cannot exceed 15")
    #max chars

    name = input("Enter your name: ")
else:
    print(f"Hello {name}")
age = int(input("What is your age: "))

while age < 16:
    print("You must be 16 or over to play this game")
    age = int(input("What is your age: \n"))
else:
     print_slow(f"Welcome to Survival, {name}\n",0.05)
print_slow("You are a deprived youth born in the slums of East London.\n",0.075)
print_slow("In order to win in life you have to choose the right choices.\n",0.075)
print_slow("These choices could either have a good or bad impact on you.\n",0.075)
print_slow("Do you have what it takes to SURVIVE. (yes/no)\n",0.25)

### Promt user for a choice
startChoice = input("> ")

if(startChoice == "no"):
    print_slow("You have forfeited, what a shame\n",0.075)

    gameover()

elif(startChoice == "yes"):
    print_slow("You are 18 years of age living in a youth hostel\n",0.075)
    print_slow("The school you go to is in Hackney, Mulburry secondary school\n",0.075)
    print_slow("You become friends with David\n",0.075)
    print_slow("Do you become friends with Jacob (yes/no)\n",0.25)
    
    friendChoice = input("> ")
    
    if(friendChoice == "yes"):
        print_slow("Jacob is in an opposing gang of david.\n",0.075)
        print_slow("This means that you inherit the 'beef' between both sides.\n",0.075)
        print_slow("David kills you; "
            "as you chose to be Jacobs friend instead of his.\n",0.075)
        gameover()

    elif(friendChoice == "no"):
        print_slow("You become friends with David instead, who is a bad "
                  "influence.\n",0.075)
        print_slow("Your 'friend', David asks if you want to skip school to,"
                   "earn money, however you know its illegal.\n",0.075)
        print_slow("Will you join him? (yes/no)\n",0.25)

    #Promt user for a choice
    moneyChoice = input("> ")

    if(moneyChoice == "yes"):
        print_slow("Your friend introduces you to his gang.\n",0.075)
        print_slow("You and his gang scheme to rob a house.\n",0.075)
        print_slow("It turns left and you are killed by the house pitbull\n",0.075)

        pitbull()

        gameover()
        exit()
            
    elif(moneyChoice == "no"):
        print_slow("Now your 'friend', David becomes your enemy\n",0.075)
        print_slow("He now wants to have a fight\n",0.075)
        print_slow("You agree to fight.\n",0.075)

# Battle System
import random

battle = True

# Class to create player character
class Player:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    # Function to attack enemies
    def attack(target):
        print("Attack")

    # Function to flee the battle
    def flee(self):
        print("Flee")

    # Function to check health
    def health_check(self):
        print("Health Check: ", self.health)
        if self.health <= 0:
            print("You died... skill issue...")
            battle = False

# Class to create enemies
class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    # Function to attack the player
    def attack(target):
        print("Attack")

    # Function to flee
    def flee(self):
        print("Flee")

    # Function to check health
    def health_check(self):
        print("Health Check: ", self.health)
        print("Enemy died... their skill issue...")
        battle = False

# Instantiates player and enemy
player = Player("Player One", 50, 50)
enemy = Enemy("Donald Trump", 200, 10)

# While the battle is ongoing, keep looping
while battle:

    #Select Player Option
    while True:
        print("'Attack or Flee'")
        player_choice = input("What do you want to do:").lower()

        if player_choice == "attack": 
            player.attack(enemy)
            break
        elif player_choice == "flee":
            player.flee()
            break
        else:
            print("Invalid option")

    enemy.health_check()

    # Select Enemy Option
    enemy_choice = random.randrange(1,2)

if enemy_choice == 1:
        enemy.attack(player)
else:
        enemy.flee()

        player.health_check()

        #If player or enemy health is equal to 0, break loop and end battle
        
        

        #Prompt user for input
        fightChoice = input("> ")

        if(fightChoice == "kick"):
            print_slow("You kick David in the head and he dies from brain damage\n",0.075)
            print_slow("You are sentenced to 4 years for manslaughter\n",0.075)
            print_slow("4 YEARS LATER...\n",0.075)
            print_slow("You are 22 now, struggling to find a job and living on the streets\n.",0.075)
            print_slow("David's gang is looking for revenge\n",0.075)
            print_slow("Will you join a gang or move cities? (gang/move)\n",0.25)

        #Prompt user for input
        moveChoice = input("> ")

        if(moveChoice == "move"):
            print_slow("You move to Birmingham; start a new life and get a job.\n",0.075)
            print_slow("5 years later...",0.075)
            print_slow("The UK is bombed by Russia....",0.075)
            print_slow("everyone dies including you....THE END.\n",0.075)

            gameover()

        elif(moveChoice == "gang"):
            print_slow("You join a gang and start selling drugs for them.\n",0.075)

            
        elif(fightChoice == "punch"):
                print_slow("David takes a gun and shoots you multiple times\n",0.075)
                print_slow("You die.\n",0.075)

                gameover()
        else :
            print("Invalid. Please enter yes or no\n")
      