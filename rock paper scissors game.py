#Input from user
#Random selection from computer
#1 for rock, 2 for paper, 3 for scissors
#Logic

import random

user_selection = int(input("Press 1 for rock, 2 for paper and 3 for scissors"))
user_choice = "initial"
comp_choice = ["Rock","Paper","Scissors"]

random_comp_choice = random.randint(0,2)

if(user_selection == 1):
    user_choice = "Rock"
elif(user_selection == 2):
    user_choice = "Paper"
else:
    user_choice = "Scissors"

#User choose rock
if(user_choice == "Rock" and comp_choice[random_comp_choice] == "Rock"):
    print("Draw")
elif(user_choice == "Rock" and comp_choice[random_comp_choice] == "Paper"):
    print("You Lose")
elif(user_choice == "Rock" and comp_choice[random_comp_choice] == "Scissors"):
    print("You Win")

#User choose paper
if(user_choice == "Paper" and comp_choice[random_comp_choice] == "Rock"):
    print("You Win")
elif(user_choice == "Paper" and comp_choice[random_comp_choice] == "Paper"):
    print("Draw")
elif(user_choice == "Paper" and comp_choice[random_comp_choice] == "Scissors"):
    print("You Lose")
    
#User choose scissors
if(user_choice == "Scissors" and comp_choice[random_comp_choice] == "Rock"):
    print("You Lose")
elif(user_choice == "Scissors" and comp_choice[random_comp_choice] == "Paper"):
    print("You Win")
elif(user_choice == "Scissors" and comp_choice[random_comp_choice] == "Scissors"):
    print("Draw")
    
print(f"Computer choose: {comp_choice[random_comp_choice]}")