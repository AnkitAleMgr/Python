from curses.ascii import isdigit
import requests, os

line_length = 138

# quality function 
def line():
    print("-" * line_length)
def custom_input(promp):
    EXIT_WORD = ("e","exit","q","quit")
    ans = input(promp).lower().strip()
    if ans in EXIT_WORD:
        exit()
    return ans

# necessery functions
def show_create_profile_and_return_selected_profile():

    # geting current, user_date folder direction
    current_dir = os.path.dirname(__file__)
    user_data_dir = current_dir + "/test_folder" # + "/user_data"
    profile_list = list()

    # region essential profile(unused)
    # def guest_profile():
    #     pass
    # def create_new_profile():
    #     pass
    # endregion

    while True:
        # region getting the name of profile and adding essential profiles
        if os.listdir(user_data_dir):    
            profile_list = os.listdir(user_data_dir) 
        profile_list.append("new")
        profile_list.insert(0, "guest")
        #  endregion

        # region displaying and asking profiles
        line()
        print("Available Profiles:")
        line()
        for index,profile in enumerate(profile_list, start= 1):
            print(f"    {index}) {profile.capitalize()}")
        line()
        while True:
            try:
                selected_profile = int(custom_input(f"Choose profile you wnat to use (1-{len(profile_list)}): ").strip())
                if 1 <= selected_profile <= len(profile_list):
                    break
                else:
                    print("Invalid option.")
            except ValueError:
                print("Invalid input format.")
        line()
        # endregion

        # region unreletaed (unused)
        # # breaking long linst in chunks of 3
        # new_profile_list = [profile_list[i:i + 3]  for i in range(0, len(profile_list), 3)]
        # # region displaying the list:
        # for row in new_profile_list:
        #     print(row)
        # endregion
        
        # region creating new profile:
        if profile_list[selected_profile -1] == "new":
            # need to create a proper folder structure(for future )
            print("Not available")
            continue
        # endregion

        # region returning selected profile
        return profile_list[selected_profile -1]
        # endregion

# mods functions
def play(path):
    print(path)
def setting():
    pass
def history():
    pass
def view_profile():
    pass

def game(profile):
    game_mods_and_options = ("Play", "Setting", "History", "View Profile", "Quit")
    
    # region locking the user choice profile path:
    if profile != "guest":
        user_profile_path  = os.path.dirname(__file__) + "/test_folder"+ f"/{profile}"
    else:
        user_profile_path = None
    # endregion

    # region Displaying all the available game mods and options:
    print("Welcome to Hang-Man")
    line()
    for index,option in enumerate(game_mods_and_options, start= 1):
        print(f"    {index}) {option}")
    # endregion
    line()
    # region asking for user game mods and proper validation checking:
    while True:
        try:
            choice = int(custom_input(f"Enter your Choice (1-{len(game_mods_and_options)}): "))
            if 1 <= choice <= len(game_mods_and_options):
                break
            else:
               print("Invalid option") 
        except ValueError:
            print("Invalid option")
        
    # endregion
    line()
    
    # region executing proper function according to user mods
    if choice == 1:
        play(user_profile_path)
    elif choice == 2:
        setting()
    elif choice == 3:
        history()
    elif choice == 4:
        view_profile()
    else:
        exit()
    # endregion


def main():
    # profile = show_create_profile_and_return_selected_profile()
    profile = "profile1"
    game(profile)

# Entry point
if __name__ == "__main__":
    main()

