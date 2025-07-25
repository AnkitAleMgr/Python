import random

length = 140
# options = ["View Rules 📜", "Play 🎮", "Game Mods ⚙️", "Records and History 🗂️", "Quit ❌"]
options = ["View Rules ", "Play ", "Game Mods ", "Records and History ", "Quit "]

# game mode setting:
no_of_dice = 2
no_of_player = 1
target_score = 100

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
def line() -> None:
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
def player_and_score_asker():
    players = []
    for i in range(no_of_player):
        name = custom_input(f"Enter {i + 1} player name: ")
        players.append(name)
    player_and_score = dict(zip(players, [0 for _ in range(len(players))]))
    return player_and_score
def score_displayer(dictionary : dict[str : int]) -> None:
    line()
    print("")
    print(" Current score :")
    print(" ----------------------------------------- ")
    print("| Player Index |"+" Player Game Name |"+" Score |")
    print("|-----------------------------------------|")
    for index ,(key, value) in enumerate(dictionary.items(), start=1):
        print("|"+f"{index:^14}"+"|"+f"{key:^18}"+"|"+f"{value:^7}"+"|")
    print(" ----------------------------------------- ")
    line()
def roll():
    rolls = []
    for i in range(no_of_dice):
        roll = random.randrange(start=1 , stop= 7 )
        rolls.append(roll)
    dice_displayer(rolls)
    for i in rolls:
        if i == 1:
            return False
    print()
    print("Your total score is",sum(rolls))

    return sum(rolls)
def dice_displayer(rolls : list):
    dice_faces = {
    1: [
        "+-------+",
        "|       |",
        "|   ●   |",
        "|       |",
        "+-------+",
        "    1    "
    ],
    2: [
        "+-------+",
        "| ●     |",
        "|       |",
        "|     ● |",
        "+-------+",
        "    2    "
    ],
    3: [
        "+-------+",
        "| ●     |",
        "|   ●   |",
        "|     ● |",
        "+-------+",
        "    3    "
    ],
    4: [
        "+-------+",
        "| ●   ● |",
        "|       |",
        "| ●   ● |",
        "+-------+",
        "    4    "
    ],
    5: [
        "+-------+",
        "| ●   ● |",
        "|   ●   |",
        "| ●   ● |",
        "+-------+",
        "    5    "
    ],
    6: [
        "+-------+",
        "| ●   ● |",
        "| ●   ● |",
        "| ●   ● |",
        "+-------+",
        "    6    "
    ]
}
    lines = [""]*6
    for roll in rolls:
        for i in range(6):
            lines[i] += dice_faces[roll][i] + "  "
    for line in lines:
        print(line)


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
def view_rules() -> None:
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
    # region basic rule displayer
    print("Basic rule:")
    print(f"   Dice : {no_of_dice}\n   Player : {no_of_player}")
    # endregion
    while True:
        line()
        change_setting = custom_input("Do you want to change setting before playing (yes/no): ")
        # line()
        if change_setting in ["yes", "y"]:
           game_mods()
           break
        elif change_setting in ["no", "n"]:
            break
        else:
            print("Invalid option. Enter 'yes' or 'no'")
    line()
    player_and_score = player_and_score_asker()
    score_displayer(player_and_score)
    # region game stated notifier
    print("")
    print("Game has been Started..")  
    print("")
    #endregion
    while not max([score for score in player_and_score.values()]) >= target_score:
        for key, value in player_and_score.items():
            running_score = 0
            print()
            print("="*length)
            print(f"{key.capitalize()} turn has started")
            print("="*length)
            print()
            while True:
                user = custom_input("Please 'r' to roll, 'b' to bank you running score and 's' to see your current score and banked score: ")
                if user == "r":
                    is_one_there = roll()
                    if is_one_there is False:
                        print()
                        print(f"{key.capitalize()} have rolled 1, so your {key.capitalize()} running score has been droped to 0 and forced to give dice to next person.")
                        running_score = 0
                        break
                    else:
                        running_score += is_one_there
                elif user == "s":
                    line()
                    print(f"Detail of {key.capitalize()}:")
                    print(f"    Running score : {running_score}")
                    print(f"    Banked score : {value}")
                    line()
                elif user == "b":
                    if running_score == 0:
                        print("You cannot bank with 0 score")
                        continue
                    player_and_score[key] = player_and_score[key] + running_score
                    line()
                    print(f"Detail of {key.capitalize()}:")
                    print(f"    Running score : {running_score}")
                    print(f"    Banked score : {value}")
                    print(f"    New Banked score : {value + running_score}")
                    line()
                    break
                else:
                    print("Invalid input.")
        score_displayer(player_and_score)       




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