from os import name
from tkinter import N
from typing import Self
from artwork import *

pegi()
survival()
name = input("What is your name? \n\n")
while name == "":
    print("You did not enter your name\n\n")
    name = input("Enter your name: \n\n")

while int(len(name)) > 15:
    print("Characters cannot exceed 15 \n\n")
    #max chars

    name = input("Enter your name: \n\n")
else:
    print(f"Hello {name}")
age = int(input("What is your age: \n\n"))

while age < 16:
    print("You must be 16 or over to play this game\n\n")
    age = int(input("What is your age: \n"))
else:
     print_slow(f"Welcome to Survival, {name}\n\n",0.05)
print_slow("You are a deprived youth born in the slums of East London.\n\n",0.075)
print_slow("In order to win in life you have to choose the right choices.\n\n",0.075)
print_slow("These choices could either have a good or bad impact on you.\n\n",0.075)
print_slow("Do you have what it takes to SURVIVE. (yes/no)\n\n",0.25)

### Promt user for a choice
startChoice = input("> ")

if(startChoice == "no"):
    print_slow("You have forfeited, what a shame\n\n",0.075)

    gameover()

elif(startChoice == "yes"):
    print_slow("You are 18 years of age living in a youth hostel\n\n",0.075)
    print_slow("The school you go to is in Hackney, Mulburry secondary school\n\n",0.075)
    print_slow("You become friends with David\n\n",0.075)
    print_slow("Do you become friends with Jacob (yes/no)\n\n",0.25)
    
    friendChoice = input("> ")
    
    if(friendChoice == "yes"):
        print_slow("Jacob is in an opposing gang of david.\n\n",0.075)
        print_slow("This means that you inherit the 'beef' between both sides.\n\n",0.075)
        print_slow("David kills you; "
            "as you chose to be Jacobs friend instead of his.\n\n",0.075)
        gameover()

    elif(friendChoice == "no"):
        print_slow("You become friends with David instead, who is a bad "
                  "influence.\n\n",0.075)
        print_slow("Your 'friend', David asks if you want to skip school to,"
                   "earn money, however you know its illegal.\n\n",0.075)
        print_slow("Will you join him? (yes/no)\n\n",0.25)

    #Promt user for a choice
    moneyChoice = input("> ")

    if(moneyChoice == "yes"):
        print_slow("Your friend introduces you to his gang.\n\n",0.075)
        print_slow("You and his gang scheme to rob a house.\n\n",0.075)
        print_slow("It turns left and you are killed by the house pitbull\n\n",0.075)

        pitbull()

        gameover()
        exit()
            
    elif(moneyChoice == "no"):
        print_slow("Now your 'friend', David becomes your enemy\n\n",0.075)
        print_slow("He now wants to have a fight\n\n",0.075)
        print_slow("You agree to fight.\n\n",0.075)
        print_slow("Will you punch or kick him? (punch/kick)\n\n",0.075)
        #Prompt user for input
        fightChoice = input("> ")

        if(fightChoice == "punch"):
            print_slow("")

        elif(fightChoice == "kick"):
            print_slow("You kick David in the head and he dies from brain damage\n\n",0.075)
            print_slow("You are sentenced to 4 years for manslaughter\n\n",0.075)
            print_slow("4 YEARS LATER...\n\n",0.075)
            print_slow("You are 22 now, struggling to find a job and living on the streets\n\n",0.075)
            print_slow("David's gang is looking for revenge\n\n",0.075)
            print_slow("Will you join a gang or move cities? (gang/move)\n\n",0.25)

        #Prompt user for input
        moveChoice = input("> ")

        if(moveChoice == "move"):
            print_slow("You move to Birmingham; start a new life and get a job.\n\n",0.075)
            print_slow("5 years later...\n\n",0.075)
            print_slow("The UK is bombed by Russia....\n\n",0.075)
            print_slow("everyone dies including you....THE END.\n\n",0.075)

            gameover()

        elif(moveChoice == "gang"):
            print_slow("You join a gang and start selling drugs for them.\n\n",0.075)
            print_slow("It's been a year of you selling drugs.\n\n")
            print_slow("You have made £50,000 in this year")
            print_slow("Will you start a legitmate business instead? (yes/no)\n\n",0.25)

        #prompt user for input
        businessChoice == input("> ")

        if(businessChoice == "yes"):
            print_slow("You start a car dealership.\n\n",0.075)
            print_slow("The business value skyrockets to £500,000 in the first year")
            print_slow("You meet a person called Nathan")
            print_slow("")

        elif(businessChoice == "no"):
            print_slow("You are murdered the next week by another dealer")
            gameover()
            

            
        elif(fightChoice == "punch"):
                print_slow("David takes a gun and shoots you multiple times\n\n",0.075)
                print_slow("You die.\n\n",0.075)


                gameover()
        else :
            print("Invalid. Please enter yes or no\n\n")
      