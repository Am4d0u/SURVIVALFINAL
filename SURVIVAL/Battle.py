from tkinter import CHAR
from weapon import fists

class Character:
    def __init__(self, 
                 name: str, 
                 health: int,
                 ) -> None:
        self.name = name
        self.health = health
        self.health_max = health

        self.weapon = fists

    def attack(self, target ) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)

        def attack(self, target) -> None:
            target.health -= self.weapon.damage
            target.health = max(target.health, 0)

hero = Hero(name= "Hero", health=100)
enemy = Enemy(name ="David", health=100)

while True:
    hero.attack(enemy)
    enemy.attack(hero)

    print(f"Health of {hero.name}: {hero.health}")
    print(f"Health of {enemy.name}: {enemy.health}")

    input()

class Hero(Character):
    def __int__(self,
                name: str,
                health: int
                ) -> None:
        super().__init__(name=name, health=health)


class Enemy(Character):
    def __int__(self,
                name: str,
                health: int
                ) -> None:
        super().__init__(name=name, health=health)


