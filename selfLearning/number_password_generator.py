import random
from Animation.Timer import Processing_animation, short_processing
from Animation.ClearScreen import screenCleaner

def main():
    length = length_asker()
    password = password_generator(length)
    display(password)

def length_asker():
    while True:
        length = input("\nLength of the password \n")
        print("")
        if length.isdigit():
            return int(length)
        else:
            print("Invalid input. Please try again \n")

def password_generator(length):
    password = ""
    # lengths = int(length)
    for i in range(length):
        # password = print(password + str(random.randint(0,9)))
        password = password + str(random.randint(0,9))
        short_processing()
        print(password)

    return password


def display(password):
    screenCleaner()
    print(f"\nYour password is:\n{password}\n")

if __name__ == "__main__":
    main()