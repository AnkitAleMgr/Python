from curses.ascii import isdigit
from traceback import print_tb


BASE_URL = "https://api.thedogapi.com/v1"
AVAILABLE_OPTION = {"search image","uplode image","list uplode image"}

length = 150

def line():
    print("-" * length)
def displayer():
   print("-"* 102)
   print(f"| {'Available Option:':<99}|")
   print("|"+"-"* 100 + "|")
   for index, i in enumerate(AVAILABLE_OPTION, start= 1):
       print(f"| {index}) {i:<96}|")
   print("-"* 102)
def custom_imput(prompt):
    EXIT_KEYWORD = ["exit","quit","q","e"]
    value = input(prompt).lower().strip()
    if value in EXIT_KEYWORD:
        exit()
    return value
def option_asker(option):
    while True:
        user_option = custom_imput(f"Choose the option(1 - {option}): ")
        if user_option.isdigit() and 1 <= int(user_option) <= option:
            return int(user_option)
        print("Invalid Option. Please try again")

def search_image():
    pass
def uplode_image():
    pass
def list_uplode_image():
    pass
def get_image_analysis():
    pass


def main():
    option = {search_image, uplode_image ,list_uplode_image}
    displayer()
    user_option_index = option_asker(len(option))
    search_image()
    

if __name__ == "__main__":
    main()