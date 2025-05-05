import time
import os


def main():
    a = True

    while a:
        value = input("\nEnter a number:")

        if value == "" or not value.isdigit():
            print("Invalid input")

        else:
            print(check_number(int(value)))

            c = True
            while c:
                again = input("\nDo you want to enter another number(yes/no): ")
                if again.lower() == "yes":
                    yes_input()
                    clear_screen()
                    c = False
                elif again.lower() == "no":
                    no_input()
                    clear_screen()
                    c = False
                    a = False
                else:
                    print("Please enter valid input")
                    # a = False

def clear_screen():
    # nt means window operating system
    # posix means mac or linux operating system
    if os.name == "nt": 
        os.system("cls")
    else:
        os.system("clear")


def check_number(value):
    a = ""
    if value % 2 == 0:
        a = "even"
    else:
        a = "odd"
    return a 


def yes_input():
    print("Processing...")
    time.sleep(1)
    print("Processing...")
    time.sleep(1)
    print("Processing...")
    time.sleep(1)
    print("\nClearing Screen.....")
    time.sleep(1)
    print("Processing...")
    time.sleep(1)
    print("Processing...")
    time.sleep(1)
    return

def no_input():
    print("Exiting ......")
    time.sleep(1)
    print("Exiting ......")
    time.sleep(1)
    print("Exiting ......")
    time.sleep(1)
    print("Sucesfully")
    print("\nClearing screen...")
    time.sleep(1)
    print("Processing...")
    time.sleep(1)
    print("Processing...")
    time.sleep(1)
    return
            

main()

# done