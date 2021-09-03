"""
File: khansole_academy.py
-------------------------
Khansole Academy is a program that teaches users how to add by asking users to input answers for the addition of two
randomly generating integers between 10 and 99 inclusive. The program returns feedback based on the User's answers.

"""

import random
# use code below  to generate a random integer between 30 and 50 for example
#print(random.randint(30, 50))

# ********************************** YOUR CODE GOES BELOW HERE *********************************************************
attempt=0
while attempt!=3:  
    number1=random.randint(20,50)
    number2=random.randint(21,60)
    add=number1+number2
    print(number1 ,'+',number2)
    ans=int(input("Enter your answer:"))
    if ans==add:
        attempt=attempt+1
        print("You have ans ", attempt , "in a row")
    else:
        print("The correct answer is ", add)
        attempt=0
print("You have mastered it !")        