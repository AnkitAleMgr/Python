# library
import random
from unittest import result

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
#global varible 
available_option = ("Choose from below 3 option: ","Rock","Paper","Scissors")
length = 100

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# functions

# result displayer
def result_displayer(result, user_choice, computer_choice):
    # beginging border
    print("-"*length)
    print(f"You choose: {available_option[int(user_choice)]}")
    print(f"Computer chose: {available_option[computer_choice]}")
    print("-"*length)
    # checking if it draw of not
    if result == "Draw":
        print(f"It is {result}")
    else:
        print(f"YOU {result}")
        
        # end border
    print("-"*length)




# logical opearation section
def logical_operation(user_choice):
    # determining loss, draw and win using matrix layout
    result_matrix = [
    [0, -1, 1],
    [1, 0, -1],
    [-1, 1, 0]  
    ]
    # computer choice using random
    computer_choice = random.randint(1,3)

    # iterate to each result_matrix
    result = result_matrix[int(user_choice) -1] [computer_choice -1]

    # passing result for display
    result_displayer("WIN" if result == 1 else "Draw" if result == 0 else "LOSE", user_choice, computer_choice)


# main section
def main():
    # making display table
    for i, option in enumerate(available_option, start=0):
        # header
        if i == 0:
            i = "▶"
            print("-"*length)
            print(f"{i:<3}{option:<10}")
            print("-"*length)
        # body 
        else:
            print(f"{i:<3}{option:<10}")
    print("-"*length)

    # forcing user to input valid input
    while True:
        print("\n" + "-"*length)
        print(f"{'▶'}{'Enter (1, 2 or 3):':>20}")
        user_choice = input(f"{"→":<3}")
        # checking for validation of input

        if user_choice == "":
            print("It cannot be empty")
        elif not user_choice.isdigit() or not 1 <= int(user_choice) <= 3:
            print("Please enter a valid number (1 to 3):")
        else:
            # sending user choice into logical section for logical operaion
            logical_operation(user_choice)
            
        
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Enrty point for program to run
if __name__ == "__main__":
    main()