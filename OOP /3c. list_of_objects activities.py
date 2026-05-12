# Learning intentions:
# - Create a list of pets
# - Use a for loop to print out various information about pets

class Pet:
    def __init__(self, name, category, age = 0):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = 'unknown'
    def __str__(self):
        payment_status = 'Unknown'
        if len(self.ccard) == 19: 
         payment_status = 'Known'
        pet_status = 'Name: ' + self.name + '\nName: ' + self.category + '\nAge: ' + str(self.age) + '\nVaccination: ' + self.vaccinated + '\nPayment Status: ' + payment_status
        return pet_status
p1 = Pet('Bonnie' , 'Dog')
p2 = Pet('Foxy', 'Cat', 7)
p3 = Pet(category = 'Rabbit', name = 'Dobby', age = 12)
p4 = Pet(name = 'Bob', age = 2, category = 'Bird')
p1.ccard = '1234 5456 9643 2467'
pets = [p1,p2,p3,p4]
for pet in pets:
   pet.vaccinated = str(True)
   print(pet)
   print('')



#ACTIVITIES:
#1. Add another pet to the list (try different methods)
#2. Vaccinate each pet in the list