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
        attack_power = random.randint(self.weapon//2, self.weapon)
        print('Attack power:', attack_power)
        return attack_power

    def skill_attack(self): #How long it takes for the attack
        attack_power = random.randint(self.weapon/2, self.weapon)
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

    def defend(self,attack_power): #When a character gets attacked, this function helps them defend the attack and calculates health loss
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
        attack_power = random.randint(self.weapon//2, self.weapon)
        attack_power += self.magic
        print(self.name + 'uses magic! ')
        print('Attack power: ', attack_power)
        return attack_power
       

class Ninja(Fighter): #Inheritence class called Ninja from Fighter Class
    def __init__(self,name,starting_health,weapon,shield,dodge,ninja_shuriken):
        super().__init__(name,starting_health,weapon,shield)
        self.dodge = dodge
        self.ninja_shuriken = ninja_shuriken
    
    def dodge_attack(self,attack_power):
        dodge_chance = random.randint(1,100)
        if dodge_chance <= self.dodge:
            print(self.name + 'dodged the attack')
        else:
            print(self.name + 'failed to dodge')
            self.defend(attack_power)

    def star(self, target): #Specific attack for this sub-class
        shuriken_chance = random.randint(1,50)
        if shuriken_chance <= self.ninja_shuriken:
         shuriken_damage = random.randint(self.ninja_shuriken//2,self.ninja_shuriken*2)
         print(self.name + 'uses his ninja shuriken!')
         print('Shuriken Damage: ' + str(shuriken_damage))
         target.defend(shuriken_damage)
        else:
         print(self.name,"'s" + 'ninja shuriken missed!')
        return target
        

class Dragon: #New class called Dragon (final boss)
    def __init__(self,name,starting_health,shield,beam):
     self.name = name
     self.__health = starting_health
     self.shield = shield
     self.beam = beam

    def report(self): #Reports Stats
        print(self.name+ ' Health: '+ str(self.__health))

    def is_dead(self): #Checks whether character is alive or dead
        if self.__health <= 0:
            return True
        else:
            return False
    
    def beam_attack(self): #Common attack for the dragon
     beam_power = random.randint(self.beam//2,self.beam)
     print('Beam Power: ' + str(beam_power))
     return beam_power

    def beam_buff(self): #When the dragon is at low health, it can make the beam attack two tiems stronger
        beam_power_buff = self.beam*2
        return beam_power_buff
    
    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage >  0:
            self.__health -= damage
            print('Damage:', damage)
        else:
            print('No damage')

    
jake = Fighter('Jake',100,28,35) #The characters statistics 
wizard = Wizard('The Grey Wizard',90,15,20,30)
ninja = Ninja('Jake The Ninja', 100, 60, 20, 35,28)
dragon = Dragon('Nocturnal Dragon', 150,50,40)

print('==============================')
print('Chapter 1')
print('==============================')
print('Sarah: See you later Jake, come tommorow!')
print("Jake: I will Sarah, don't you worry")
print('Jake starts walking outside the martial arts centre, when he finds a red cube lying on the floor')
print('Jake: What is this?')
print('Jake touches the cube...and suddenly, a blue portal appears out of nowhere, sucking up Jake and his soul, as he travels through dimensions and dimensions, until he reaches an unknown dimension...')
input('Press ENTER or RETURN to continue ')

print('==============================')
print('Chapter 2')
print('==============================')
print('Jake: Where am I?')
print('*Footsteps approach Jake*')
print('Sarah: Oh hey Jake! It looks like you reached the Nocturnal World')
print('Jake: The Nocturnal World??? Sarah, what are you doing here anyway?')
print("Sarah: Don't you worry about me Jake, but there's something you must worry about, the ancient relic of futurity")
print('Jake: What is that thing?')
print("Sarah: It's a red-looking cube, don't stress too much Jake, you will be just fine.")
print('*Jake is left baffled. He starts walking towards an abandoned building, when he suddenly feels an ominous surge through his veins*')
print('What was that?')
print('*Jake, confused as ever, continues walking, but as he starts walking, a wizard appears out of thin air*')
print('Wha-, who are you?')
print('*The wizard, without speaking a word, fires a magic beam at Jake, which he barely dodges*')
print('Well, here we go...')
input('Press ENTER or RETURN to continue ')

print('==============================')
print('Chapter 3')
print('==============================')
while True:
 jake = Fighter('Jake',100,28,35) #The characters statistics (need to put this in true loop so that player health can reset)
 wizard = Wizard('The Grey Wizard',90,15,20,30)
 ninja = Ninja('Jake The Ninja', 100, 60, 20, 35,28)
 dragon = Dragon('Nocturnal Dragon', 150,50,40)

 Answer = input('Do you choose to be a Fighter or a Ninja? 1. Fighter 2. Ninja ')
 if Answer == '1':
  current_jake = jake
 else:
    current_jake = ninja
 print('Let the showdown begin!')
 while not current_jake.is_dead() and not wizard.is_dead():
  current_jake.report()
  wizard.report()
  Option = input('Choose your move: 1. Regular Attack 2. Skill Attack 3. Ninja Shuriken 4. Dodge (only pick 3 or 4 if you are a ninja) ') 
  if Option == '1':
   dmg = current_jake.random_attack()
   wizard.defend(dmg)
  elif Option == '2':
   dmg = current_jake.skill_attack()
   wizard.defend(dmg)
  elif Option == '3':
   dmg = current_jake.star(wizard)
  elif Option == '4':
   wizard_dmg = wizard.random_attack()
   current_jake.dodge_attack(wizard_dmg)
   current_jake.healing()
  if wizard.is_dead():
   break
  wizard_dmg = wizard.random_attack()
  current_jake.defend(wizard_dmg)
  current_jake.healing()
 if current_jake.is_dead():
  print('You lost, now try again!')
 if wizard.is_dead():
  print("You won, congratulations! Let's move on to the next part of your journey!")
  break

print('==============================')
print('Chapter 4')
print('==============================')
print('Jake: Oh man, I feel like my back is about to break! That really was a tough fight.')
