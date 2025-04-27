import random

print("Guess the b number in dice:")
print("Are you ready to play")

a = True

def roll_dice():
    b = True
    
    while b:
        random_Number = random.randint(1,6)
        guess = input("Enter your guess: ")
        
        if guess == "":
            print("\nPlease enter a number.")
        
        elif int(guess) == random_Number:
            print("\nYou have guess the right number.")
            b = False
            
        else:
            print("\nBetter luck next time")
        

while a:
    x = input("\nPlease enter yes/no: \n")
    
    if x == "":
        print("\nYou cannot put empty.")
        x = ""
        
    elif x.lower() == "yes":
        print("\nLet start")
        roll_dice()
    
    else:
        print("\nLet play next time.")
        a = False