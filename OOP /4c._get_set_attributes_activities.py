class Pet:
    def __init__(self, name, category, breed = None, age = 0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0
    
    def get_weight(self):
        return self.weight
    
    def set_weight(self):
        if self.weight == int or float:
         return self.weight
        

#ACTIVITIES:
#1. Add attribute weight and write a getter method for weight
#2. Add setter method on weight and make sure it is a positive number (integer or float)