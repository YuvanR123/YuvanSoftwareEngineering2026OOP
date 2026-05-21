#Learning Intentions
#1. Create a defend method that helps you repel an attack
#2. Create a loop which simulates a fight and declares a winner
#3. Test the game 

import random, time 

class Fighter: #Making class for fighter
 def __init__(self, name, starting_health, weapon, shield):
    self.name = name
    self.health = starting_health
    self.weapon = weapon
    self.shield = shield

 def random_attack(self): #Makes a new define function for a random attack using random input
   attack_power = random.randint(int(self.weapon/2), int(self.weapon*2))
   print('Attack Power: ' + str(attack_power))
   return attack_power
 
 def defend(self,attack_power):
    self.attack_power = attack_power
    damage = self.shield - attack_power
    if damage > 0:
     self.health -= damage
     print('Damage: ' + str(damage))
    else:
     print('No damage received')
   


 def report(self): #This is for the stats of the fighter
   print(self.name + ' Health: ' + str(self.health))


fighter1 = Fighter('Jack', 100, 90, 50) 
fighter2 = Fighter('Monkey', 200, 60, 120) #All fighter stats including name, starting health, weapon and shield
fighter1.report()
fighter2.report()

while True:
 print('Jack attacks Monkey!') 
 fighter2.defend(fighter1.random_attack())
 fighter2.report()
 time.sleep(1)
 if fighter2.health < 0:
   fighter2.health = 0
   print ('Jack has won this battle!')
   break


  
   