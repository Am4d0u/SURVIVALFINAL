import random

def battle(player, enemy):
    # Battle System
    # While the battle is ongoing, keep looping
    battle = True

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
        enemy_choice = 1

        if enemy_choice == 1:
            enemy.attack(player)
        elif enemy_choice == 2:
            player.health_check()


    #If player or enemy health is equal to 0, break loop and end battle



# Class to create player character
class Player:
    def __init__(self, name, health, damage):
        self.name = name  
        self.health = health
        self.damage = damage

    # Function to attack enemies
    def attack(self, target):
        print("Attack")
        target.health -= 50

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
    def attack(self, target):
        print("Attack")
        target.ealth -= 50

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

