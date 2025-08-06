import random, logging, os, json, ast
from traceback import print_tb

length = 140
options = ["View Rules ", "Play ", "Game Mods ", "Records and History ", "Quit"]

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
def setting_loder():
    global no_of_dice, target_score, no_of_player
    default_settings = {
    "no of dice": 2,
    "no of player": 4,
    "target score": 100
}
    setting_file_path = os.path.dirname(os.path.abspath(__file__)) + "/setting.json"
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
    global no_of_dice, target_score, no_of_player
    while True:
        user_input = custom_input(f"Enter the {key} ({min_max[0]} - {min_max[1]}): ")
        if  user_input.isdigit() and (1 <= int(user_input) <= min_max[1]):
            break
        print("Invalid input")
    if key == "no of dice":
        no_of_dice = int(user_input)
        line()
        print(f"Number of dice has been changed into {user_input}")
    elif key == "no of players":
        no_of_player = int(user_input)
        print(f"Number of Player has been changed into {user_input}")
    elif key == "target score":
        target_score = int(user_input)
        print(f"Target score has been changed into {user_input}")
    else:
        print("something went wrong.")
        print("Exiting..")
        exit()
    setting_saver()
def setting_saver():
    global no_of_dice, target_score, no_of_player
    new_setting = {
    "no of dice": no_of_dice,
    "no of player": no_of_player,
    "target score": target_score
    }

    setting_file_path = os.path.dirname(os.path.abspath(__file__)) + "/setting.json"
    with open(setting_file_path, "w") as f:
        json.dump(new_setting, f, indent= 4)


def mode_asker():
    line()
    print("Welcome to Pig game:")
    line()
    for index, option in enumerate(options, start=1):
        print(str(index)+")", option)
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
        "target score": [[100, 500], "number"]
    }
    
    print("    Available mods: ")
    for index, mod in enumerate(mods, start=1):
        print(f"    {index}) {mod}")
    print("")

    while True:
        try:
            option = int(custom_input(f"Enter the index of option you want to chagen (1 - {len(mods)}): "))
        except:
            print("Invalid input")
            line()
            continue
        if not (1 <= option <= len(mods)):
            print("Invalid option")
            line()
            continue
        key = [key for key in mods][option - 1]
        min_max, number = mods[key]
        setting_changer(key, min_max, number)
        break
def play():
    # region basic rule displayer
    print("Basic rule:")
    print(f"   Dice : {no_of_dice}\n   Player : {no_of_player} \n   Target Score : {target_score}")
    # endregion
    while True:
        line()
        change_setting = custom_input("Do you want to change setting before playing (yes/no): ")
        line()
        if change_setting in ["yes", "y"]:
           game_mods()
        elif change_setting in ["no", "n"]:
            break
        else:
            print("Invalid option. Enter 'yes' or 'no'")
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

    logger(player_and_score)
def records_and_history():
    path = os.path.dirname(os.path.abspath(__file__))+ "/history.log"        
    try:
        if os.path.exists(path):
            with open(path, "r") as f:
                content = f.read()
        else:
            raise FileNotFoundError
    except FileNotFoundError as e:
        print("Error : ",e)

    # clearing terminal
    if os.name == "nt":
        os.system("clr")
        os.system("clr")
    else:
        os.system("clear")
        os.system("clear")
    # seprating the data
    for lines in content.splitlines():
        # printing data
        try:
            date, info_type, score = lines.split(" - ")
            score = ast.literal_eval(score)
            print()
            print(f"Date: {date[:19]}")
            print("------------------------")
            print("|"+"   Name   "+"|"+"   Score   "+"|")
            print("------------------------")
            for name, point in score.items():
                print(f"|{name.capitalize():^10}|{point:^11}|")
            print("------------------------")
        except Exception as e:
            print("Invalid data format found in histroy", e)
            print("Exiting..")
            exit()


def main():
    # records_and_history()
    setting_loder()
    while True:
        mode = mode_asker()
        match mode:
            case 1:
                view_rules()
            case 2:
                play()
            case 3:
                game_mods()
            case 4:
                records_and_history()
            case 5:
                print("Exiting...")
                line()
                exit()

if __name__ == "__main__":
    main()
