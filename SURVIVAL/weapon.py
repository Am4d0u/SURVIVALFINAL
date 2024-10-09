class Weapon:
    def __init__(self, 
                name: str,
                weapon_type: str,
                damage: int, 
                value: int
                ) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

Zombie_knife = Weapon(name="Zombie Knife",
                      weapon_type="sharp",
                      damage=5,
                      value=10)

Gun = Weapon(name ="Gun",
             weapon_type="ranged",
             damage=6,
             value=12)

fists = Weapon(name = "Fists",
               weapon_type="blunt",
               damage=2,
               value=0)

