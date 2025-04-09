#Script for Tip Calculator
Total_amount = int(input("What is the tota amount in the bill?"))
Num_of_people = int(input("In how many people does this bill splits into?"))
Percentage_in_tip = int(input("What percentage of the total bill do you wish to give the tip in total?"))
Total_tip = ((Percentage_in_tip)/100)*Total_amount
Tip_per_person = round(Total_tip/Num_of_people, 2)
print(f"Your total tip would be: {Total_tip}, tip per person would be: {Tip_per_person}")
