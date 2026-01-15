
# Exercise
# 1. Create a hero class with 2 parameters: damage, monster
# 2. The monster class should have a method that lowers the health -> get_damage(amount)
# 3. Hero class should have an attack method that calls the get_damage method from the monster, the amount of 
#damage is hero.damage

class Hero:

    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster


    def attack(self):
        self.monster.get_damage(self.damage)


class Monster:

    def __init__(self,health,energy):
        self.health = health
        self.energy = energy
    
    def update_energy(self,amount):
        self.amount += amount
    
    def get_damage(self, amount):
        self.health -= amount
    

monster = Monster(health = 100, energy = 50)

hero = Hero(damage = 15, monster = monster)

print(monster.health)
hero.attack()
print(monster.health)