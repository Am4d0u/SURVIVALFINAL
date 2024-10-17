import time
import os
import random
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
    print("SURVIVAL")
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

# Function for additional encounters
def random_encounter(name, game_speed):
    encounters = [
        "You find a wallet on the ground. Do you take it or return it? "
        "(take/return)",
        "You meet an old friend who offers you drugs. Do you accept or "
        "decline? (accept/decline)",
        "A stray dog approaches you. Do you pet it or ignore it? (pet/ignore)"
    ]

    encounter = encounters[random.randint(0, len(encounters) - 1)]
    print_slow(encounter, game_speed)

    choice = input("> ")

    if "take" in choice:
        print_slow("You took the wallet. It's filled with cash!\n", game_speed)
    elif "return" in choice:
        print_slow("You returned the wallet. The owner rewards you with "
                   "gratitude!\n", game_speed)
    elif "accept" in choice:
        print_slow("You accepted the drugs. It leads you down a dark path...\n", 
                   game_speed)
        gameover()
    elif "decline" in choice:
        print_slow("You declined the offer and chose to stay clean.\n", 
                   game_speed)
    elif "pet" in choice:
        print_slow("The dog becomes your loyal companion!\n", game_speed)
    elif "ignore" in choice:
        print_slow("You ignored the dog and it walks away.\n", game_speed)

# Main game logic
def main():
    game_speed = display_speed_menu()  # Get game speed from the user
    clear_console()

    pegi()
    survival()
    
    name = input("What is your name? \n\n")
    while not name:
        print("You did not enter your name\n\n")
        name = input("Enter your name: \n\n")

    while len(name) > 15:  # Max characters
        print("Characters cannot exceed 15 \n\n")
        name = input("Enter your name: \n\n")

    age = int(input("What is your age: \n\n"))

    while age < 16:
        print("You must be 16 or over to play this game\n\n")
        age = int(input("What is your age: \n"))

    print_slow(f"Welcome to Survival, {name}\n\n", game_speed)
    print_slow("You are a deprived youth born in the slums of East London.\n\n", 
               game_speed)
    print_slow("To win in life, you have to choose the right choices.\n\n", 
               game_speed)
    print_slow("These choices could have a good or bad impact on you.\n\n", 
               game_speed)
    print_slow("Do you have what it takes to SURVIVE? (yes/no)\n\n", 
               game_speed)

    start_choice = input("> ")

    if start_choice.lower() == "no":
        print_slow("You have forfeited; what a shame.\n\n", game_speed)
        gameover()

    elif start_choice.lower() == "yes":
        print_slow("You are 18 years old living in a youth hostel.\n\n", 
                   game_speed)
        print_slow("The school you go to is in Hackney, Mulberry Secondary "
                   "School.\n\n", game_speed)
        print_slow("You become friends with David.\n\n", game_speed)
        print_slow("Do you become friends with Jacob? (yes/no)\n\n", 
                   game_speed)

        friend_choice = input("> ")

        if friend_choice.lower() == "yes":
            print_slow("Jacob is in an opposing gang of David.\n\n", game_speed)
            print_slow("This means that you inherit the 'beef' between both sides.\n"
                       "\n", game_speed)
            print_slow("David kills you; as you chose to be Jacob's friend.\n\n", 
                       game_speed)
            gameover()

        elif friend_choice.lower() == "no":
            print_slow("You become friends with David instead, who is a bad influence.\n\n", 
                       game_speed)
            print_slow("Your 'friend', David asks if you want to skip school to "
                       "earn money; however, you know it's illegal.\n\n", game_speed)
            print_slow("Will you join him? (yes/no)\n\n", game_speed)

            money_choice = input("> ")

            if money_choice.lower() == "yes":
                print_slow("Your friend introduces you to his gang.\n\n", game_speed)
                print_slow("You and his gang scheme to rob a house.\n\n", game_speed)
                print_slow("It turns left, and you are killed by the house pit bull.\n\n", 
                           game_speed)
                pitbull()
                gameover()

            elif money_choice.lower() == "no":
                print_slow("You end up fighting David.\n", game_speed)
                print_slow("Type 'fight' to initiate it.\n",game_speed)
              
                fight_choice = input("> ")

                if fight_choice.lower() == "fight":
                    # Define the battle
                    hero = Hero(name)  # Create the protagonist
                    enemy = Enemy("David")  # Create the enemy
                    print_slow("A fight breaks out between you and David!\n", game_speed)

                    # Battle Loop
                    while hero.health > 0 and enemy.health > 0:
                        print_slow(f"\n{hero.name}'s Health: {hero.health} - "
                                   f"{enemy.name}'s Health: {enemy.health}\n", 
                                   game_speed)
                        action = input("Choose your action (punch/kick): ").lower()

                        if action == "punch":
                            hero.punch(enemy)
                            print_slow(f"You punched {enemy.name}!\n", game_speed)
                        elif action == "kick":
                            hero.kick(enemy)
                            print_slow(f"You kicked {enemy.name}!\n", game_speed)
                        else:
                            print_slow("Invalid action! You lose your turn.\n", 
                                       game_speed)

                        # Enemy's turn
                        if enemy.health > 0:
                            enemy.attack(hero)
                            print_slow(f"{enemy.name} attacks you!\n", game_speed)

                    # Battle Result
                    if hero.health > 0:
                        print_slow("You killed David!\n\n", game_speed)
                        print_slow("You are sentenced to 4 years for manslaughter.\n\n", 
                                   game_speed)
                        print_slow("4 YEARS LATER...\n\n", game_speed)
                        print_slow("You are 22 now, struggling to find a job and living "
                                   "on the streets.\n\n", game_speed)
                        print_slow("David's gang is looking for revenge.\n\n", game_speed)
                        print_slow("Will you join a gang or move cities? (gang/move)\n\n", 
                                   game_speed)

                        move_choice = input("> ")

                        if move_choice.lower() == "move":
                            print_slow("You move to Birmingham; start a new life and get a "
                                       "job.\n\n", game_speed)
                            print_slow("5 years later...\n\n", game_speed)
                            print_slow("The UK is bombed by Russia...\n\n", game_speed)
                            print_slow("Everyone dies including you....THE END.\n\n", 
                                       game_speed)
                            gameover()

                        elif move_choice.lower() == "gang":
                            print_slow("You join a gang and start selling drugs for them.\n\n", 
                                       game_speed)
                            print_slow("It's been a year of you selling drugs.\n\n", 
                                       game_speed)
                            print_slow("You have made £50,000 in this year.\n\n", 
                                       game_speed)

                            # Random encounter during the gang phase
                            random_encounter(name, game_speed)

                            print_slow("Do you want to continue in the gang or leave it? "
                                       "(continue/leave)\n", game_speed)
                            gang_choice = input("> ")

                            if gang_choice.lower() == "continue":
                                print_slow("You rise through the ranks, but the law is "
                                           "closing in.\n", game_speed)
                                print_slow("A rival gang ambushes you. Fight or flee? "
                                           "(fight/flee)\n", game_speed)
                                
                                ambush_choice = input("> ")

                                if ambush_choice.lower() == "fight":
                                    print_slow("You bravely fight but get caught in a crossfire.\n", 
                                               game_speed)
                                    gameover()
                                elif ambush_choice.lower() == "flee":
                                    print_slow("You escape but are now on the run. Life "
                                               "becomes tough.\n", game_speed)
                                    print_slow("You end up living in hiding for years.\n", 
                                               game_speed)
                                    gameover()

                            elif gang_choice.lower() == "leave":
                                print_slow("You decide to leave the gang. It's a tough choice.\n", 
                                           game_speed)
                                print_slow("You try to get a normal job, but your past haunts you.\n", 
                                           game_speed)
                                print_slow("Will you tell the truth about your past or lie on "
                                           "your resume? (truth/lie)\n", game_speed)

                                truth_choice = input("> ")

                                if truth_choice.lower() == "truth":
                                    print_slow("You honestly reveal your past. They respect your "
                                               "honesty.\n", game_speed)
                                    print_slow("You get the job! Congratulations!\n", game_speed)
                                    gameover()
                                elif truth_choice.lower() == "lie":
                                    print_slow("You lie on your resume. They find out and fire "
                                               "you.\n", game_speed)
                                    gameover()

# Start the game
if __name__ == "__main__":
    main()