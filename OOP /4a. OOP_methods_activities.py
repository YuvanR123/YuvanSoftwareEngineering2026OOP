# Learning intentions:
# - Create a method (function belonging to a class)
# - Discuss the use of attributes in the method

class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'Unknown'
        self.vaccinated = False
        self.account_balance = 'Unknown'

    def vaccinate(self):
        self.vaccinated = True

    def __str__(self):
        if self.vaccinated:
            return '\nName: ' + self.name + '\nType: ' + self.category + '\nAge: ' + str(self.age) + '\nVaccinate: ' + 'Bonnie is vaccinated'
        else:
            return '\nName: ' + self.name + '\nType: ' + self.category + '\nAge: ' + str(self.age) + '\nVaccinate: ' + 'Bonnie is not vaccinated. Please vaccinate her now'
        
    def human_age(self):
        if self.category == 'Dog':
            print(self.name,'human age: ', self.age*7)
        elif self.category == 'Cat':
            print(self.name,'human age: ',self.age*6)
        else:
            print(self.name,'human age is unknown')

    def have_birthday(self):
        self.age += 1
    
    def clear_account_balance(self):
        self.account_balance = 0

p1 = Pet('Bonnie', 'Cat', 12,)
p1.have_birthday()
p1.vaccinate()
print(p1)
p1.human_age()
    
    

#ACTIVITIES:
#1. Add another method to vaccinate the pet
#2. Add another attribute for account balance then add a method to clear balance
#3. Add a method to print the animals age in human years use a multiplier of 7 if animal is a dog and a multiplier of 6 if it is a cat
# Use print statements to ensure you have comeplted each activity correctly.