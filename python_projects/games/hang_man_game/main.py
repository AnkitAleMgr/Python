from curses.ascii import isdigit
import requests, os

line_length = 140

def line():
    print("-" * line_length)
def custom_input(promp):
    EXIT_WORD = ("e","exit","q","quit")
    ans = input(promp).lower().strip()
    if ans in EXIT_WORD:
        exit()
    return ans
def show_create_profile():

    # geting current, user_date folder direction
    current_dir = os.path.dirname(__file__)
    user_data_dir = current_dir + "/test_folder" # + "/user_data"
    profile_list = list()

    # region essential profile(unused)
    def guest_profile():
        pass
    def create_new_profile():
        pass
    # endregion

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

    # region identifing selected profile from user
    
    # endregion




def main():
    show_create_profile()


# Entry point
if __name__ == "__main__":
    main()

