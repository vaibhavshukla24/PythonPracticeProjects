height = int(input("Please enter your height in cm: "))
bill = 0
if(height > 120):
    print("You are allowed to ride")
    age = int(input("Please enter your age: "))
    
    if(age < 12):
        bill = 10
        print("Your ticket price is $10")
    elif(age >= 12 and age < 18):
        bill = 12
        print("Your ticked price is $12")
    else:
        print("Your ticket price is $15")
        bill = 15
        
    want_photograph = str(input("Do you want a photograph? "))
    
    if(want_photograph == "Yes"):
        bill += 2
        print("This will add $2 to your existing bill")
        print(f"Your final bill is ${bill}")
    else:
        print("Your bill remains the same")
        print(f"Your final bill is ${bill}")
else:
    print("You are not allowed to ride")