#This is an example of creating and calling a function which does not return anything
def greet():
    print("Hello coders")
    print("This is a greeting function")
    print("Good going!!")

greet()

#Now I am creating a function with an input
def greet_inp(name):
    print(f"Greetings {name}")

#I am passing the paramerter as pass by value    
name_for_greeting = str(input("Please enter the name of the person you would like to greet: "))
greet_inp(name_for_greeting)

#Functions with more than one input
def greet_with_multi_inp(name, location):
    print(f"Greetings {name}")
    print(f"How is it going there in {location}")
    
name_3 = str(input("Please enter your name: "))
location_3 = str(input("Please enter your location: "))

#Observe that we have changed the positions of the arguments but have bind these arguments with the keyword as present in the function definition. These are called keyword arguments
greet_with_multi_inp(location = location_3, name =  name_3)