name = 'Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
ccard = '3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 2695'
owner_name = 'Alex Ngyuen'
account_balance = 129.95

def help():
  print('Welcome to the Pet Data Management System')
  print("Every vet's best friend")

def increase_age():
  global age
  age = age + 1

def verify_credit_card(card_num):
  if len(card_num) == 19:
    if len(card_num.split()) == 4:
      return True
  return False


help()
increase_age()
print(age)


#ACTIVITIES:
#There are many ways to complete these. How will you go about the job?
#1. Verify this number 1234 4334 1001 0000
#2. Ask the user for a credit card number and let them know if it is valid
#3. If the credit card is valid then reduce balance by $39
#4. Write and test a function to vaccinate Bonnie 

c_card_number = '1234 4334 1001 0000'
if verify_credit_card(c_card_number) == True:
  print('VALID')
else:
  print('INVALID')
new_card_number = input('What is your credit card number? ')
if verify_credit_card(new_card_number) == True:
  print('VALID')
  account_balance = account_balance - 39
else:
  print('INVALID')

def check_vaccinate_bonnie(): 
    Question = input('Is bonnie vaccinated? ')
    if Question == 'Yes' or Question == 'yes':
      print('Bonnie is vaccinated')
    else:
      print('Bonnie is not vaccinated. Vaccinate her now please.')
check_vaccinate_bonnie()
