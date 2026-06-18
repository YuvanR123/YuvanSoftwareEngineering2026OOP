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
        attack_power = random.randint(self.weapon//2, self.weapon*2)
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
     if self.__health < 25:
      heal_amount = random.randint(2,10)
      self.__health += heal_amount
      print(self.name, 'healed ', heal_amount)
     else:
      print(self.name, 'had no amount healed')

      
class Wizard(Fighter): #Inheritance class called Wizard from the Fighter Class
    def __init__(self,name, starting_health, weapon, shield,magic):
        super().__init__(name, starting_health, weapon, shield)
        self.magic = magic

    def random_attack(self):
        attack_power = random.randint(self.weapon//2, self.weapon)
        attack_power += self.magic
        print(self.name + ' uses magic! ')
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
            print(self.name + ' dodged the attack')
        else:
            print(self.name + ' failed to dodge')
            self.defend(attack_power)

    def star(self, target): #Specific attack for this sub-class
        shuriken_chance = random.randint(1,50)
        if shuriken_chance <= self.ninja_shuriken:
         shuriken_damage = random.randint(self.ninja_shuriken//2,self.ninja_shuriken*2)
         print(self.name + ' uses his ninja shuriken!')
         print('Shuriken Damage: ' + str(shuriken_damage))
         target.defend(shuriken_damage)
        else:
         print(self.name + "'s ninja shuriken missed!")
        return target
        

class Dragon: #New class called Dragon (final boss)
    def __init__(self,name,starting_health,shield,beam):
     self.name = name
     self.__health = starting_health
     self.shield = shield
     self.beam = beam

    def report(self): #Reports Stats
        print(self.name + ' Health: '+ str(self.__health))

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
    def get_health(self):
       return self.__health
    
jake = Fighter('Jake',100,40,15) #The characters statistics 
wizard = Wizard('The Grey Wizard',80,25,18,20)
ninja = Ninja('Jake The Ninja', 90, 35, 10, 45,30)
dragon = Dragon('Nocturnal Dragon', 180,20,35)

def Chapter_1_Script():
 print('Welcome to...The Martial Vagabond. This game is about a young martial artist destined to enlighten the present state of Earth.')
 time.sleep(6)
 print('He travels to another dimension, fighting wizards, dragons and most importantly...himself. Sit back, relax and enjoy! (and good luck)')
 time.sleep(6)
 print('==============================')
 print('Chapter 1')
 print('==============================')
 time.sleep(4)
 print('* The atmosphere is dusty, covered with a dark sky, destroyed houses and bright artificial lights aiming directly at the city centre *')
 time.sleep(5)
 print("Sarah: What a world we live in now huh...the meteor got to the best of us.")

 print("Jake: I know Sarah...A world where families could live peacefully and happily is now only a dystopian land with corruption")
 time.sleep(3)
 print("Jake: I swear Sarah, someday, I will make this world the way it used to be, no...I will make it better than before. Mark my words.")
 time.sleep(3)
 print("Sarah: It's not impossible, so I hope everyone's future the best. Okay then, see you later Jake, come back tommorow!")
 time.sleep(3)
 print("Jake: I will Sarah, don't you worry!")
 time.sleep(2)
 print(' * Jake starts walking outside the martial arts centre, when he finds a red cube lying on the floor *')
 time.sleep(2)
 print('Jake: What is this?')
 time.sleep(2)
 print('* Jake touches the cube...and suddenly, a blue portal appears out of nowhere, sucking up Jake and his soul, as he travels through dimensions and dimensions, until he reaches an unknown dimension *')
 time.sleep(3)
 input('Press ENTER or RETURN to continue ')

Chapter_1_Script()
def Chapter_2_Script():
 print('==============================')
 print('Chapter 2')
 print('==============================')
 time.sleep(4)
 print('Jake: Where am I?')
 print('* Footsteps approach Jake *')
 time.sleep(2)
 print('The World God: Oh hey Jake! It looks like you reached the Nocturnal World')
 time.sleep(2)
 print('Jake: The Nocturnal World??? Who are you?')
 time.sleep(2)
 print("The World God: Don't you worry about me Jake, but there's something you must worry about, the ancient relic of futurity.")
 time.sleep(2)
 print('Jake: What is that thing?')
 time.sleep(2)
 print("The World God: It's a red-looking cube, for all you need to know. I'll give you a little hint, it's the cure to humanities problems. Don't stress too much over it. Ok Bye!")
 time.sleep(4)
 print('* Jake is left baffled. He starts walking towards an abandoned building, when he suddenly feels an ominous surge through his veins *')
 time.sleep(4)
 print('Jake: What was that?')
 time.sleep(2)
 print('* Jake, confused as ever, continues walking, but as he starts walking, a wizard appears out of thin air *')
 time.sleep(3)
 print('Jake: Wha-, who are you?')
 time.sleep(2)
 print('* The wizard, without speaking a word, fires a magic beam at Jake, which he barely dodges *')
 time.sleep(2)
 print('Jake: Well, here we go...')
 time.sleep(2)
 input('Press ENTER or RETURN to continue ')
Chapter_2_Script()
print('==============================')
print('Chapter 3')
print('==============================')
time.sleep(4)
while True:
 jake = Fighter('Jake',100,40,15) #The characters statistics (need to put this in a loop so that player healths reset)
 wizard = Wizard('The Grey Wizard',80,25,18,20)
 ninja = Ninja('Jake The Ninja', 90, 35, 10, 45,30)
 dragon = Dragon('Nocturnal Dragon', 180,20,35)

 Answer = input('Do you choose to be a Fighter or a Ninja? 1. Fighter 2. Ninja (input number corresponding to option) ')
 if Answer == '1':
  current_jake = jake
 elif Answer == '2':
    current_jake = ninja
 else:
    print('Invalid choice, setting choice as Fighter')
    current_jake = jake
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
   if isinstance(current_jake,Ninja):
    current_jake.star(wizard)
   else:
      print('This move is only for ninjas!')
  elif Option == '4':
   if isinstance(current_jake,Ninja):
    wizard_dmg = wizard.random_attack()
    current_jake.dodge_attack(wizard_dmg)
    current_jake.healing()
  else:
   print('This move is only for ninjas!') 
  if wizard.is_dead():
    break
  wizard_dmg = wizard.random_attack()
  current_jake.defend(wizard_dmg)
  current_jake.healing()
 if current_jake.is_dead():
  print('You lost, now try again!')
 if wizard.is_dead():
  print("You won, congratulations! Let's move on to the next part of your journey!")
  input('Press ENTER or RETURN to continue! ')
  break
def Chapter_4_Script():
 print('==============================')
 print('Chapter 4')
 print('==============================')
 time.sleep(4)
 print('Jake: Oh man, I feel like my back is about to break! That really was a tough fight.')
 time.sleep(2)
 print('* Jake starts heading towards the centre of the city, where he sees neon-lit abandoned buildings around him and a spellcast magic circle in the centre plaza *')
 time.sleep(3)
 print('Jake: This is a really crowded city huh...')
 time.sleep(2)
 print('* Suddenly, out of nowhere, a nocturnus dragon spawns in the middle of the spellcast magic circle *')
 time.sleep(2)
 print("* It's piercing red blood-shot eyes and the hard white/green scales that the dragon posesses makes Jake shiver *")
 time.sleep(3)
 print("Jake: Oh...hi, what's your name?")
 time.sleep(2)
 print('* The dragon blasts a swift blue beam that almost hits Jake, burning his left ankle as he swiftly dodges the attack *')
 time.sleep(3)
 print("Jake: You aren't too friendly dragon, let me help you with your manners.")
 time.sleep(2)
Chapter_4_Script()
while True:
 jake = Fighter('Jake',100,40,15) #The characters statistics (need to put this in a loop so that player healths reset)
 wizard = Wizard('The Grey Wizard',80,25,18,20)
 ninja = Ninja('Jake The Ninja', 90, 35, 10, 45,30)
 dragon = Dragon('Nocturnal Dragon', 180,20,35)
 Answer = input("Do you choose to be a Fighter or a Ninja? 1. Fighter 2. Ninja ")
 if Answer == '1': 
   current_jake = jake
 elif Answer == '2':
   current_jake = ninja
 else:
    print('Invalid choice, setting choice as Fighter')
    current_jake = jake
 beam_buffed = False
 print('Let the fight begin!')
 while not current_jake.is_dead() and not dragon.is_dead():
  current_jake.report()
  dragon.report()
  X = input('Choose your move: 1. Regular Attack 2. Skill Attack 3. Ninja Shuriken 4. Dodge (Pick 3 and 4 only if ninja) ')
  time.sleep(2)
  if X == '1':
    dmg = current_jake.random_attack()
    dragon.defend(dmg)
  elif X == '2':
   dmg = current_jake.skill_attack()
   dragon.defend(dmg)
  elif X == '3':
   if isinstance(current_jake,Ninja):
    dmg = current_jake.star(dragon)
   else:
      print('This move is only for Ninjas!')
  elif X == '4':
   if isinstance(current_jake,Ninja):
    dragon_dmg = dragon.beam_attack()
    current_jake.dodge_attack(dragon_dmg)
    current_jake.healing()
   else:
      print('This move is only for Ninjas!')
 if dragon.is_dead():
    break
 if dragon.get_health() <= 20 and not beam_buffed:
  dragon.beam_buff()
  beam_buffed = True
  print('The dragon uses a super-charged beam!')
 dragon_dmg = dragon.beam_attack()
 current_jake.defend(dragon_dmg)
 current_jake.healing()
 if current_jake.is_dead():
    print('You lose the final battle. Sending you back now!')
 if dragon.is_dead():
    print('You beat the final battle of this story! Congratulations!')
    input('Press ENTER or RETURN to continue! ')
    break
def Chapter_5_Script():
 print('==============================')
 print('Chapter 5')
 print('==============================')
 time.sleep(4)
 print("Jake: I don't think I can move anymore...")
 time.sleep(2)
 print("Dragon of Wisdom: You did well human, better than I expected...")
 time.sleep(2)
 print("Jake: YOU CAN TALK???")
 time.sleep(2)
 print("Dragon of Wisdom: Of course, we are pretty similar to humans you see.")
 time.sleep(2)
 print("Jake: Yeah, clearly.")
 time.sleep(2)
 print("Dragon of Wisdom: So tell me human, why did you come to the Nocturnus World?")
 time.sleep(2)
 print("Jake: Well I am looking for a red cube")
 time.sleep(2)
 print("Dragon of Wisdom: The ancient relic of futurity. I thought you were looking for that. ")
 time.sleep(2)
 print("* Suddenly, the red cube appears in front of Jake's feet *")
 time.sleep(2)
 print("Dragon of Wisdom: Since you won this battle, I will let you have it. Once you use it, it will disappear, so don't worry. I hope it solves everyone's problems back in your world.")
 time.sleep(4)
 print("Jake: Well, I sure hope it does. Thank you Dragon.")
 time.sleep(2)
 print("Dragon of Wisdom: You are welcome here anytime, if you want to come back, just think about this place and the cube will appear in front of you in no time.")
 time.sleep(4)
 print("Jake: Okay, thank you so much!")
 time.sleep(2)
 print("*The red cube projects a light shining beam throughout the area, warping Jake into a time lapse and bringing him back to his world*")
 time.sleep(4)
 print("* Jake wakes up and looks around in the world he is currently in *")
 time.sleep(2)
 print("* This can't be my world, there is no way...it looks just like the past *")
 time.sleep(3)
 print("Sarah: Jake? Oh my god! You have been missing for 10 days, where were you?")
 time.sleep(2)
 print("Jake: I will tell you all that later but can you first tell me, where are we? Another multi-dimension?")
 time.sleep(3)
 print("Sarah: What are you talking about? This is Earth, your home.")
 time.sleep(2)
 print("Jake: Has it always been like this?")
 time.sleep(2)
 print("Sarah: Uhm...yes it has Jake, you must be really sick. Now let's go get some food!")
 time.sleep(2)
 print("* Jake tries his best to act normal, but within, he is holding his tears back *")
 time.sleep(2)
 print("Jake: Sure Sarah. Let's go get some food!")
 time.sleep(2)
 print("* Jake's journey had come to an end. He travelled an entire dimension, met gods and fought right until it was all over. Now, he had saved the world. *")
 time.sleep(5)
 print(" ^This is the story of the saviour of the world. The silent hero. The Martial Vagabond^")
 time.sleep(4)
 print('THE END')
Chapter_5_Script()