#Learning Intentions
#1. Create a loop which simulates a fight and declares a winner
#2. Test the game 
#3. Implement the game with a private __health attribute

import random

class Fighter:
 def __init__(self, name, starting_health, weapon, shield):
    self.name = name
    self.health = starting_health
    self.weapon = weapon
    self.shield = shield

 def random_attack(self):
   attack_power = random.randint(self.weapon*2, self.weapon/2)
   print('Attack Power: ' + attack_power)
   return attack_power

 def report(self):
   print(self.name + 'Health: ' + str(self.health))


   
fighter1 = Fighter('Jack', 100, 90, 50)
fighter2 = Fighter('Monkey', 200, 60, 120)
fighter1.report()
fighter2.report()
print('Fighter 1 attacks Fighter 2!')
fighter2.health -= fighter1.random_attack()
fighter2.report()


