# Learning intentions:
# - Create a car class example
# - Use attributes: make, model, year and price
# - Create a __str__ method that prints make and model

class Car:
    def __init__(self,make,model,year, wheels, price = None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.for_sale = 'Unknown'
        self.wheels = wheels
        

    def __str__(self): 
        return '\nMake :' + self.make + '\nModel :' + self.model + '\nYear :' + self.year + '\nWheels: ' + self.wheels + '\nPrice: ' + str(self.price) + '\nSale: ' + self.for_sale 

        

c1 = Car(make = 'Mazda', wheels = 'GTR Wheels', model = '6', year = '2005')
c1.for_sale = 'For Sale' #For things that are not inside the parameter, you must change it seperately like this (since for sale isn't in the starting parameter)
c2 = Car('Volvo', 'XC40', '2022', 'Volvo Wheels', '$100,000')
c2.for_sale = 'For Sale'
c3 = Car('Lamborghini', 'Aventador', '2012', 'Sports Car Wheels', '$312,000' )
c3.for_sale = 'Not For Sale'



cars = [c1,c2,c3]

for car in cars:
    print(car)


#ACTIVITIES:
#1. Istantiate another car object
#2. Add another attribute (for_sale)
#3. Add sale status for sale or not for sale to the __str__ method
#4. Create 2 more cars and print all car statuses with a loop