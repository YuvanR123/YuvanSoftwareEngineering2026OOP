# Learning intentions:
# - Create a class pet with same information as in previous examples
# - Create an object instance of class pet
class Pet:
    def __init__(self,name,age,category,vaccinated):
        self.name = name
        self.age = age
        self.category = category
        self.vaccination = vaccinated
        self.creditcard = "unknown"
        self.billingaddress = "unknown"
        self.ownername = "unknown"
        self.accountbalance = 0
    

p1 = Pet('Bonnie', 5, 'Chicken', True)
print(p1.name)
print(p1.age)
print(p1.category)
p2 = Pet('Foxy', 3, 'Dog', True)

print(p2.name)
print(p2.age)
print(p2.category)
print(p2.vaccination)
print(p2.billingaddress)




#ACTIVITIES:
#1. Print out vaccination status of Bonnie
#2. Create another pet named Foxy who is a dog
#3. Add the following attributes to the pet class:
# - credit card
# - billing address
# - owner name (preset to unknown)
# - account balance (pre set to 0)