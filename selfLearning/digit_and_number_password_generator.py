import random
import time
from Animation.ClearScreen import screenCleaner
from Animation.Timer import Processing_animation
from number_password_generator import length_asker

def main():
    length = length_asker()
    password = password_generator(length)
    display(password)

def password_generator(length):
    number = "1234567890"
    letter = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    special_charecter = "!@#$%^&*()_+-=[]|;:,.<>?/"

    all_charecter = number + letter + special_charecter
    password = ""
    # Processing_animation()
    # for i in range(length):
    #     time.sleep(0.05)
    #     password += random.choice(all_charecter)
    #     print(password)
    print("Generating password", end="", flush=True)
    for i in range(length):
        time.sleep(0.05)
        password += random.choice(all_charecter)
        print(".", end="", flush=True)
    print()

    return password

def display(password):
    screenCleaner()
    print("Password is: ")
    print(password)
    print()

if __name__ == "__main__":
    main()