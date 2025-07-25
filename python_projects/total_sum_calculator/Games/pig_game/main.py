from random import randrange
import random

length = 140
# options = ["View Rules 📜", "Play 🎮", "Game Mods ⚙️", "Records and History 🗂️", "Quit ❌"]
options = ["View Rules ", "Play ", "Game Mods ", "Records and History ", "Quit "]

# game mode setting:
no_of_dice = 2
no_of_player = 2

def symbols():
    """
+-------+      +-------+      +-------+
|       |      | ●     |      | ●   ● |
|   ●   |      |   ●   |      |       |
|       |      |     ● |      | ●   ● |
+-------+      +-------+      +-------+
    1              2              3

+-------+      +-------+      +-------+
| ●   ● |      | ●   ● |      | ●   ● |
|       |      |   ●   |      | ●   ● |
| ●   ● |      | ●   ● |      | ●   ● |
+-------+      +-------+      +-------+
    4              5              6

    """
def line():
    print("-"*length)
def custom_input(prompt):
    EXIT_SYMBOL = ["q", "quit", "exit","e"]
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in EXIT_SYMBOL:
            print("Exiting....")
            line()
            exit()
        if user_input == "":
            print("Empty input. Please fill the detail. ")
            line()
            continue
            
        return user_input

def mode_asker():
    line()
    print("Welcome to Pig game:")
    line()
    for index, option in enumerate(options, start=1):
        print(str(index)+")" , option)
    line()
    while True:
        mode = custom_input(f"Enter the your choice(1-{len(options)}): ")

        if not mode.isdigit() or not  1 <= int(mode) <= len(options):
            print("Invalid option. Please try again.")
            line()
            continue
        line()
        break
    return int(mode)
def view_rules():
    pig_game_description = """
    🎲 Pig Game (Dice Game):
    Pig is a simple turn-based dice game for two or more players. The goal is to be the first to reach 100 points.

    🛠️ How it works:
    - On your turn, roll a dice as many times as you like.
    - Each roll adds to your turn score.
    - If you roll a 1, your turn ends and your turn score is lost.
    - You can choose to "hold" (end your turn voluntarily) and add your turn score to your total score.
    - Then, it’s the next player’s turn.

    🏆 Win Condition:
     - First player to reach 100 points wins!`

    🎮 Game Customization:
     - The game can be customized with options like the number of players, goal points, penalties, and more through Game Modes.
       Explore the Game Modes section to discover all available settings! 
"""
    print(pig_game_description)
def game_mods():
    print("Game mods will be available soon")
def play():
    # print("Basic rule:")
    # print(f"   Dice : {no_of_dice}\n   Player : {no_of_player}")
    # while True:
    #     line()
    #     change_setting = custom_input("Do you want to change setting before playing (yes/no): ")
    #     # line()
    #     if change_setting in ["yes", "y"]:
    #        game_mods()
    #        break
    #     elif change_setting in ["no", "n"]:
    #         break
    #     else:
    #         print("Invalid option. Enter 'yes' or 'no'")
    # line()
    # print("")
    # print("Game has been Started..")  

    
    
    # rolls = []
    # for i in range(no_of_dice):
    #     roll = random.randrange(start=1 , stop= 7 )
    #     rolls.append(roll)
def main():
    # while True:
    #     mode = mode_asker()
    #     match mode:
    #         case 1:
    #             view_rules()
    #         case 2:
    #             play()
    #         case 3:
    #             game_mods()
    #         case 4:
    #             records_and_history()
    #         case _:
                # print("Exiting...")
                # line()
                # exit()
     play()    

if __name__ == "__main__":
    main()