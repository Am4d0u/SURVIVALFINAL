class Character:
    def __init__(self, name, health):
        self.name = name
        self.max_health = health
        self.health = health

    def is_alive(self):
        return self.health > 0

    def display_health(self):
        health_percentage = (self.health / self.max_health) * 100
        health_bar_length = 20  # Length of the health bar
        filled_length = int(health_bar_length * health_percentage // 100)
        bar = '█' * filled_length + '-' * (health_bar_length - filled_length)
        print(f"{self.name} Health: |{bar}| {self.health}/{self.max_health}")

class Hero(Character):
    def __init__(self, name):
        super().__init__(name, health=100)  # Hero starts with 100 health

    def punch(self, enemy):
        damage = 10  # Damage dealt
        enemy.health -= damage
        print(f"{self.name} punches {enemy.name} for {damage} damage!")
        enemy.display_health()

    def kick(self, enemy):
        damage = 15  # Damage dealt
        enemy.health -= damage
        print(f"{self.name} kicks {enemy.name} for {damage} damage!")
        enemy.display_health()

class Enemy(Character):
    def __init__(self, name):
        super().__init__(name, health=50)  # Enemy starts with 50 health

    def attack(self, hero):
        damage = 10  # Damage dealt
        hero.health -= damage
        print(f"{self.name} attacks {hero.name} for {damage} damage!")
        hero.display_health()

# Example usage:
if __name__ == "__main__":
    hero = Hero("Hero")
    enemy = Enemy("Enemy")

    hero.display_health()
    enemy.display_health()

    # Simulating a battle
    hero.punch(enemy)
    enemy.attack(hero)
    hero.kick(enemy)
    enemy.attack(hero)