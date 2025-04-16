#Storing prices of the pizza based on size
small_pizza_price = 15
medium_pizza_price = 20
large_pizza_price = 25

#Storing prices of the pepperoni based on size
pepperoni_small_price = 2
pepperoni_med_or_large_price = 3

#Storing extra cheese price
extra_cheese_price = 1

#Creating a bill variable; Initialising it with value 0
bill = 0

#Storing the user input for size, pepperoni choice and extra cheese choice
pizza_size = str(input("Please enter the pizza size you require; S for small, M for medium and L for large pizza: "))
pepperoni_choice = str(input("Please enter if you wish to add pepperoni in the pizza; Y for yes, N for no: "))
extra_cheese_choice = str(input("Please enter Y if you want extra cheese else enter N: "))

#Adding the amount to bill based on the choice of the size of pizza
if(pizza_size == "S"):
    bill += small_pizza_price
elif(pizza_size == "M"):
    bill += medium_pizza_price
else:
    bill += large_pizza_price

#Adding the amount to the bill based on the choice of pepperoni
if(pizza_size == "S" and pepperoni_choice == "Y"):
    bill += pepperoni_small_price
elif(pizza_size != "S" and pepperoni_choice == "Y"):
    bill += pepperoni_med_or_large_price

#Adding the amount of extra cheese based on the user's choice    
if(extra_cheese_choice == "Y"):
    bill += extra_cheese_price

#printing the final bill
print(f"Your final price for the pizza is ${bill}.")
