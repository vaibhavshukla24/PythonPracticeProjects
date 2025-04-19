#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

my_password = ""

#Appending letters to password
for i in range(0,nr_letters):
    my_password += random.choice(letters)

#Appending numbers to the password
for i in range(0,nr_numbers):
    my_password += random.choice(numbers)
    
#Appending symbols to the password
for i in range(0,nr_symbols):
    my_password += random.choice(symbols)


#Printing the password
print(my_password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hard_pass = []

#Appending letters to password
for i in range(0,nr_letters):
    hard_pass.append(random.choice(letters))

#Appending numbers to the password
for i in range(0,nr_numbers):
    hard_pass.append(random.choice(numbers))
    
#Appending symbols to the password
for i in range(0,nr_symbols):
    hard_pass.append(random.choice(symbols))

random.shuffle(hard_pass)

final_password = ""

for i in range(0, len(hard_pass)):
    final_password += hard_pass[i]

print(final_password)
    