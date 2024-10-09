import time
import os
from artwork import *
from Battle import Hero, Enemy

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print slowly
def print_slow(message, delay=0.05):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # Print a newline at the end

# Function to display the game speed menu and get speed choice
def display_speed_menu():
    clear_console()
    print("Welcome to the Game Speed Menu")
    print("Choose the game speed:")
    print("1. Fast")
    print("2. Normal")
    print("3. Slow")
    
    choice = input("Enter your choice (1, 2, 3): ")
    
    if choice == '1':
        return 0.05  # Fast speed
    elif choice == '2':
        return 0.1   # Normal speed
    elif choice == '3':
        return 0.25  # Slow speed
    else:
        print("Invalid choice, please select again.")
        return display_speed_menu()

# Function for game over
def gameover():
    print_slow("Game Over! Thanks for playing!", 0.05)
    exit()

# Function to present a choice and return the user's input
def choose(options):
    while True:
        choice = input(f"Choose an option {options}: ")
        if choice in options:
            return choice
        else:
            print("Invalid choice, please try again.")

# Main game logic
def main():
    game_speed = display_speed_menu()  # Get game speed from the user
    clear_console()
    
    pegi()
    survival()
    name = input("What is your name? \n\n")
    while name == "":
        print("You did not enter your name\n\n")
        name = input("Enter your name: \n\n")

    while len(name) > 15:  # max chars
        print("Characters cannot exceed 15 \n\n")
        name = input("Enter your name: \n\n")
        
    age = int(input("What is your age: \n\n"))

    while age < 16:
        print("You must be 16 or over to play this game\n\n")
        age = int(input("What is your age: \n"))

    print_slow(f"Welcome to Survival, {name}\n\n", game_speed)
    print_slow("You are a deprived youth born in the slums of East London.\n\n", game_speed)
    print_slow("In order to win in life you have to choose the right choices.\n\n", game_speed)
    print_slow("These choices could either have a good or bad impact on you.\n\n", game_speed)
    print_slow("Do you have what it takes to SURVIVE? (yes/no)\n\n", game_speed)

    startChoice = input("> ")

    if startChoice.lower() == "no":
        print_slow("You have forfeited, what a shame\n\n", game_speed)
        gameover()

    elif startChoice.lower() == "yes":
        print_slow("You are 18 years of age living in a youth hostel\n\n", game_speed)
        print_slow("The school you go to is in Hackney, Mulberry Secondary School\n\n", game_speed)
        print_slow("You become friends with David\n\n", game_speed)
        print_slow("Do you become friends with Jacob? (yes/no)\n\n", game_speed)

        friendChoice = input("> ")

        if friendChoice.lower() == "yes":
            print_slow("Jacob is in an opposing gang of David.\n\n", game_speed)
            print_slow("This means that you inherit the 'beef' between both sides.\n\n", game_speed)
            print_slow("David kills you; as you chose to be Jacob's friend instead of his.\n\n", game_speed)
            gameover()

        elif friendChoice.lower() == "no":
            print_slow("You become friends with David instead, who is a bad influence.\n\n", game_speed)
            print_slow("Your 'friend', David asks if you want to skip school to earn money; however, you know it's illegal.\n\n", game_speed)
            print_slow("Will you join him? (yes/no)\n\n", game_speed)

            moneyChoice = input("> ")

            if moneyChoice.lower() == "yes":
                print_slow("Your friend introduces you to his gang.\n\n", game_speed)
                print_slow("You and his gang scheme to rob a house.\n\n", game_speed)
                print_slow("It turns left and you are killed by the house pit bull.\n\n", game_speed)
                gameover()

            elif moneyChoice.lower() == "no":
                print_slow("You end up fighting David\n", game_speed)
                print_slow("Do you want to fight him or run away? (fight/run)\n", game_speed)

                fightChoice = input("> ")

                if fightChoice.lower() == "fight":
                    # Define the battle
                    hero = Hero(name)  # Create the protagonist
                    enemy = Enemy("David")  # Create the enemy
                    print_slow("A fight breaks out between you and David!\n", game_speed)
                    
                    # Battle Loop
                    while hero.health > 0 and enemy.health > 0:
                        print_slow(f"\n{hero.name}'s Health: {hero.health} - {enemy.name}'s Health: {enemy.health}\n", game_speed)
                        action = input("Choose your action (punch/kick): ").lower()
                        
                        if action == "punch":
                            hero.punch(enemy)
                            print_slow(f"You punched {enemy.name}!\n", game_speed)
                        elif action == "kick":
                            hero.kick(enemy)
                            print_slow(f"You kicked {enemy.name}!\n", game_speed)
                        else:
                            print_slow("Invalid action! You lose your turn.\n", game_speed)

                        # Enemy's turn
                        if enemy.health > 0:
                            enemy.attack(hero)
                            print_slow(f"{enemy.name} attacks you!\n", game_speed)

                    # Battle Result
                    if hero.health > 0:
                        print_slow("You defeated David!\n\n", game_speed)
                        print_slow("You are sentenced to 4 years for manslaughter.\n\n", game_speed)
                        print_slow("4 YEARS LATER...\n\n", game_speed)
                        print_slow("You are 22 now, struggling to find a job and living on the streets.\n\n", game_speed)
                        print_slow("David's gang is looking for revenge.\n\n", game_speed)
                        print_slow("Will you join a gang or move cities? (gang/move)\n\n", game_speed)

                        moveChoice = input("> ")

                        if moveChoice.lower() == "move":
                            print_slow("You move to Birmingham; start a new life and get a job.\n\n", game_speed)
                            print_slow("5 years later...\n\n", game_speed)
                            print_slow("The UK is bombed by Russia...\n\n", game_speed)
                            print_slow("Everyone dies including you....THE END.\n\n", game_speed)
                            gameover()

                        elif moveChoice.lower() == "gang":
                            print_slow("You join a gang and start selling drugs for them.\n\n", game_speed)
                            print_slow("It's been a year of you selling drugs.\n\n", game_speed)
                            print_slow("You have made £50,000 in this year.\n\n", game_speed)
                            print_slow("Will you start a legitimate business instead? (yes/no)\n\n", game_speed)

                            businessChoice = input("> ")

                            if businessChoice.lower() == "yes":
                                print_slow("You start a car dealership.\n\n", game_speed)
                                print_slow("The business value skyrockets to £500,000 in the first year.\n\n", game_speed)
                                print_slow("You meet a person called Nathan.\n\n", game_speed)
                                print_slow("Nathan: 'I can help you increase the scale of your business by x10.'\n\n", game_speed)
                                print_slow("You: 'How will you do that?'\n\n", game_speed)
                                print_slow("Nathan: 'I have a couple of friends in the government that control the billboards in the middle of major cities, which will most certainly get your business the publicity it needs to spread nationwide.'\n\n", game_speed)
                                print_slow("Nathan: 'This publicity will bring an influx of 100% more customers, including celebrities and major figures.'\n\n", game_speed)
                                print_slow("You: 'What is the catch?'\n\n", game_speed)
                                print_slow("Nathan: 'I need to own 50% shares of this business.'\n\n", game_speed)
                                print_slow("Will you accept this offer? (yes/no)\n\n", game_speed)

                                accept_choice = choose(["yes", "no"])
                                if accept_choice == "yes":
                                    print_slow("You accept Nathan's offer and your business thrives.\n\n", game_speed)
                                    print_slow("You become a prominent figure in the car industry!\n\n", game_speed)
                                    print_slow("Congratulations! You've successfully navigated through the challenges.\n\n", game_speed)
                                    gameover()
                                else:
                                    print_slow("You refuse Nathan's offer and decide to keep your business to yourself.\n\n", game_speed)
                                    print_slow("A rival dealer feels threatened and arranges a hit on you...\n\n", game_speed)
                                    gameover()

                            elif businessChoice.lower() == "no":
                                print_slow("You are murdered the next week by another dealer.\n\n", game_speed)
                                gameover()

                elif fightChoice.lower() == "run":
                    print_slow("You chose to run away from David!\n\n", game_speed)
                    print_slow("You find a safe spot and reflect on your life choices...\n\n", game_speed)
                    print_slow("You decide to change your life for the better.\n\n", game_speed)
                    print_slow("Will you pursue education or a job? (education/job)\n\n", game_speed)

                    lifeChoice = input("> ")

                    if lifeChoice.lower() == "education":
                        print_slow("You enroll in a college and work hard.\n\n", game_speed)
                        print_slow("Years pass and you graduate with honors.\n\n", game_speed)
                        print_slow("You land a great job and leave your past behind!\n\n", game_speed)
                        print_slow("Congratulations! You have successfully turned your life around.\n\n", game_speed)
                        gameover()

                    elif lifeChoice.lower() == "job":
                        print_slow("You take a low-paying job but work hard to save up.\n\n", game_speed)
                        print_slow("With dedication, you climb up the ladder and start your own business.\n\n", game_speed)
                        print_slow("You become successful and inspire others!\n\n", game_speed)
                        gameover()

# Start the game
if __name__ == "__main__":
    main()
