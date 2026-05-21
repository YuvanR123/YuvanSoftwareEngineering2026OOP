#Learning Intentions
#1. Create a loop which simulates a fight and declares a winner
#2. Test the game 
#3. Implement the game with a private __health attribute

import random

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

 def report(self): #This is for the stats of the fighter
   print(self.name + ' Health: ' + str(self.health))


   
fighter1 = Fighter('Jack', 100, 90, 50) 
fighter2 = Fighter('Monkey', 200, 60, 120) #All fighter stats including name, starting health, weapon and shield
fighter1.report()
fighter2.report()
print('Jack attacks Monkey!') 
fighter2.health -= fighter1.random_attack()
fighter2.report()
print('To be continued...')
#In my early version of making this code, this error message came up  File "/usr/lib/python3.12/random.py", line 312, in randrange, istop = _index(stop), TypeError: 'float' object cannot be interpreted as an integer
#I did not know what to do because this is from the backend of the code and I cannot edit anything since I don't have permission
#Now I figured out the problem, I had to add int functions to my (attack_power =) line since they are represented as floats, and i had to swap the multiply and divide because python needs the smaller numbers first. Lastly, I had to change the attack power print statement to a str function. This was a good learning experience!