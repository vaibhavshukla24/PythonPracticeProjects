'''
You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

2. Then check for the number of times the letters in the word LOVE occurs.   

3. Then combine these numbers to make a 2 digit number and print it out. 

e.g.

name1 = "Angela Yu" name2 = "Jack Bauer"

T occurs 0 times 

R occurs 1 time 

U occurs 2 times 

E occurs 2 times 

Total = 5 

L occurs 1 time 

O occurs 0 times 

V occurs 0 times 

E occurs 2 times 

Total = 3 



Love Score = 53
'''

def calculate_love_score(name_1, name_2):
    combined_name = name_1 + name_2
    
    total_1 = 0
    total_2 = 0
    
    word_1 = "TRUE"
    word_2 = "LOVE"
    
    for letter in combined_name.upper():
        if letter in word_1:
            total_1 += 1
    
    for letter in combined_name.upper():
        if letter in word_2:
            total_2 += 1
    
    print(f"{total_1}{total_2}")
    
name_1 = str(input("Enter name 1: "))
name_2 = str(input("Enter name 2: "))
calculate_love_score(name_1, name_2)