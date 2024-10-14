# battle.py

class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0

class Hero(Character):
    def __init__(self, name):
        super().__init__(name, health=100)  # Hero starts with 100 health

    def punch(self, enemy):
        damage = 10  # Damage dealt
        enemy.health -= damage

    def kick(self, enemy):
        damage = 15  # Damage dealt
        enemy.health -= damage

class Enemy(Character):
    def __init__(self, name):
        super().__init__(name, health=50)  # Enemy starts with 50 health

    def attack(self, hero):
        damage = 10  # Damage dealt
        hero.health -= damage
