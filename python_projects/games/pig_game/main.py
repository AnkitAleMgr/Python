from encodings.punycode import T
from operator import setitem
import random, logging, os, json

length = 140
# options = ["View Rules 📜", "Play 🎮", "Game Mods ⚙️", "Records and History 🗂️", "Quit ❌"]
options = ["View Rules ", "Play ", "Game Mods ", "Records and History ", "Quit ,"]

# setting = None

# no_of_dice = setting["no_of_dice"]
no_of_dice = None
no_of_player = None
target_score = None

def line() -> None:
    print("-"*length)
def custom_input(prompt):
    EXIT_SYMBOL = ["q", "quit", "exit", "e", "clear"]

    while True:
        user_input = input(prompt).strip().lower()
        if user_input in EXIT_SYMBOL:
            print("Exiting....")
            line()
            exit()
        if user_input == "":
            print("Empty input. Please fill the detail. ")
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
def logger(data : list):
    path = os.path.join(os.path.dirname(__file__), "history.log")

    logging.basicConfig(
    level=logging.INFO,
    filename= path,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info(data)
def winner_notifier(data : list):
    sorted_data = dict(sorted(data.items(), key=lambda items: items[1], reverse= True))
    rank = 0
    previous_value = None
    ranked = dict()

    for key, value in sorted_data.items():
        if value != previous_value:
            rank += 1
            previous_value = value
        ranked[key] = rank   
    # region ddisplaying output
    print("-"*29)
    print(f"|{"Name":^10}|{"Rank":^6}|{"Score":^9}|")
    print("|"+"-"*27+ "|")
    for key, rank in ranked.items():
        print(f"|{key:^10}|{rank:^6}|{sorted_data[key]:^9}|")
    print("-"*29)
    # endregion
def no_of_dice_changer():
    global no_of_dice
    while True:
        try:
            dice = int(custom_input("Enter the no of dice you want to play with (1- 10): "))
        except ValueError:
            print("Invalid input.")
        if not (1 <= dice <= 10):
            print(f"{dice} cannot be accepted.")
            continue
        no_of_dice = dice
        print(f"No of dice has been changed to {dice}")
        return
def no_of_player_changer():
    pass
def target_score_changer():
    pass
def setting_loder():
    global no_of_dice, target_score, no_of_player
    default_settings = {
    "no of dice": 2,
    "no of player": 4,
    "target score": 100
}
    setting_file_path = os.path.dirname(os.path.abspath(__file__)) + "/setting.json"
    print(setting_file_path)
    while True:
        if os.path.exists(setting_file_path):
            print("File found. Loding data...")
            with open(setting_file_path, "r") as f:
                setting = json.load(f)
                break
        else:
            print("File doesnt exist. New file 'setting.json' has been created.")
            with open (setting_file_path, "w") as f:
                json.dump(default_settings, f, indent=4)
    no_of_dice = setting["no of dice"]
    no_of_player = setting["no of player"]
    target_score = setting["target score"]
def setting_changer(key, min_max, number):
    print("got it")
    print(key, min_max, number)
    

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
    mods = {
        "no of dice" : [[1, 10], "number"],
        "no of players": [[1, 10], "number"],
        "target score": [[1, 10], "number"]
    }
    
    print("    Available mods: ")
    for index, mod in enumerate(mods, start=1):
        print(f"    {index}) {mod}")
    print("")
    # while True:
    #     try:
    #         index = int(custom_input(f"Enter the mod index you want to change(1-{ len(mods)}): "))
    #     except ValueError:
    #         print("invalid input.")
    #         continue
    #     if not (0 < int(index) <= len(mods)):
    #         print("Invalid option please try again")
    #     else:
    #         function = mods_function[index -1]
    #         function()
    #         break
    
    while True:
        try:
            option = int(custom_input(f"Enter the index of option you want to chagen (1 - {len(mods)}): "))
        except:
            print("Invalid input")
        if not (1 <= option <= len(mods)):
            print("Invalid option")
        key = [key for key in mods][option - 1]
        min_max, number = mods[key]
        print(key, min_max, number)
        print(type(key))
        print(type(min_max))
        print(type(number))

        setting_changer(key, min_max, number)
        break

        
        


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
    winner_notifier(player_and_score)
    print("Game has  ended")

    # logger(player_and_score)


def main():
    # setting_loder()
    game_mods()


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
    #             print("Exiting...")
    #             line()
    # player_and_score = {'ankit': 752, 'anmol': 111, 'vim': 75,'ankits': 5, 'anmols': 11, 'vims': 752}
    # winner_notifier(player_and_score)

if __name__ == "__main__":
    main()
