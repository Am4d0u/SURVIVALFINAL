﻿from artwork import *

survival()

print_slow("Welcome to Survival\n",0.05)
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
        print_slow("You lose all popularity.\n",0.075)
        print_slow("David kills you because you chose to be Jacobs friend instead of his.\n",0.075)
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
        print_slow("It turns left and you are killed", 
               "by the house owner's pitbull \n",0.075)
        pitbull()

        gameover()
            
       
    elif(moneyChoice == "no"):
        print_slow("Now your 'friend', David becomes your enemy\n",0.075)
        print_slow("He now wants to have a fight\n",0.075)
        
        
        print_slow("You agree to fight, will you kick him in the face",
              "or punch him in the stomach? (kick/punch)\n",0.25)

        #Prompt user for input
        fightChoice = input("> ")

        if(fightChoice == "kick"):
            print_slow("You kick David in the head and he dies from brain damage\n",0.075)
            print_slow("You are sentenced to 3 years for manslaughter\n",0.075)
            print_slow("3 YEARS LATER...\n",0.075)
            print_slow("You are 22 now, struggling to find a job and living on the streets\n.",0.075)
            print_slow("David's gang is looking for revenge.\n",0.075)
            print_slow("Will you join a gang or move cities? (gang/move)\n",0.25)

        #Prompt user for input
        moveChoice = input("> ")

        if(moveChoice == "move"):
            print_slow("You move to Birmingham; start a new life and get a job.\n",0.075)
            print_slow("5 years later...The UK is bombed by Russia....",
               "everyone dies including you....THE END.\n",0.075)

        elif(moveChoice == "gang"):
            print_slow("You join the opposing gang and start selling drugs for them.\n",0.075)

            
        elif(fightChoice == "punch"):
                print_slow("David takes out a gun and shoots you multiple times\n",0.075)
                print_slow("You die.\n",0.075)

                gameover()
        else :
                      print("Invalid. Please enter yes or no\n")

    else :
        print("Invalid. Please enter yes or no\n")
        
        
 
    

 