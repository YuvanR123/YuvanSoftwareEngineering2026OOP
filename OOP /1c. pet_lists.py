#Tutorial 3 Lists:
#1. Create an example of parallel lists eg: pet_name, species, age, vaccination_status for three pets
pet_names = ['Bruce', 'Sarah', 'Bob', 'Hootie']
species = ['Dog', 'Cat', 'Bird', 'Blowfish']
age = [3,6,2,34]
vaccination_status = [True, True, False, True]
#2. Use a for loop to print parallel list details. This will mean that one complete printout will look like:
'''
Pet name: Foxy
Species: Dog
Age: 8
Vaccination Status: False
'''
for i in range(len(pet_names)):
 print('Pet name: ', pet_names[i])
 print('Species: ', species[i])
 print('Age: ', age[i])
 print('Vaccination Status: ', vaccination_status[i])
#3. Demonstrate what happens when an item is deleted
'''
IndexError: list index out of range
'''
print('Okay, let us vaccinate Bob the Parrot now')
  #ACTIVITIES:
# In each activity test out that the printing of data is still valid
#1. Add a new animal named Hootie, its a blowfish, it is 34 years
#2. Vaccinate an unvaccinated animal (create vaccination)
#3. Remove an animal and make sure that all the printing is correct
pet_names = ['Bruce', 'Bob', 'Hootie']
species = ['Dog', 'Bird', 'Blowfish']
age = [3,2,34]
vaccination_status = [True, False, True]