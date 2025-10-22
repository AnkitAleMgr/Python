import requests, os

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

    # essential profile
    def guest_profile():
        pass
    def create_new_profile():
        pass

    # getting the name of profile names and adding essential profiles
    if os.listdir(user_data_dir):    
        profile_list = os.listdir(user_data_dir) 
    profile_list.append("new")
    profile_list.insert(0, "guest")

    # breaking long linst in chunks of 3
    new_profile_list = [profile_list[i:i + 3]  for i in range(0, len(profile_list), 3)]
    # region displaying the list:
    for row in new_profile_list:
        
    # endregion



    

def main():
    show_create_profile()


# Entry point
if __name__ == "__main__":
    main()

