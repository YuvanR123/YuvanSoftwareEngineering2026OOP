import random, time 

class Fighter: # Sets a new class called 'Fighter' for the fighter game
    def __init__(self,name, starting_health, weapon, shield):
        self.name = name
        self.__health = starting_health
        self.weapon = weapon
        self.shield = shield
  
    def report(self): #Reports Stats
        print(self.name+':'+ ' Health: '+ str(self.__health))

    def is_dead(self): #Checks whether character is alive or dead
        if self.__health <= 0:
            return True
        else:
            return False

    def random_attack(self): #Gives character a random attack power
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        print('Attack power:', attack_power)
        return attack_power

    def skill_attack(self): #How long it takes for the attack
        attack_power = random.randint(self.weapon/2, self.weapon*2)
        target = random.randint(2,6)
        print('Hit enter in exactly',target,'seconds')
        tic = time.time()
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 3 - abs(target-time_taken)
        if multiplier < 2: 
            multiplier = 0

        print('Attack power:', attack_power)
        print('Multiplier:', multiplier)
        return int(attack_power*multiplier)

    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')
    
    def healing(self): #Define function that does automatic healing when character is low
     if self.__health < 20:
      heal_amount = random.randint(2,10)
      self.__health += heal_amount
      print(self.name, 'healed ', heal_amount)
     else:
      print(self.name + 'had' + 'no amount healed')

      
class Wizard(Fighter): #Inheritance class called Wizard from the Fighter Class
    def __init__(self,name, starting_health, weapon, shield,magic):
        super().__init__(name, starting_health, weapon, shield)
        self.magic = magic

    def random_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon*2)
        attack_power += self.magic
        print(self.name + 'uses magic! ')
        print('Attack power: ', attack_power)
        return attack_power
       

class Ninja(Fighter): #Inheritence class called Ninja from Fighter Class
    def __init__(self,name,starting_health,weapon,shield,dodge):
        super().__init__(name,starting_health,weapon,shield)
        self.dodge = dodge
    
    def dodge_attack(self,attack_power):
        dodge_chance = random.randint(1,100)
        if dodge_chance <= self.dodge:
            print(self.name + 'dodged the attack')
        else:
            print(self.name + 'failed to dodge')
            self.defend(attack_power)

jake = Fighter('Jake',100,60,20)
wizard = Wizard('The Grey Wizard',160,30,10,50)
ninja = Ninja('Jake The Ninja', 90, 70, 60, 35)


