from Animation.Loding_animation import advance_loding_animation
import traceback, string, random

# function: 

def print_line(char='-', width=152):
    print(char * width)


def encrypt():
    try:
        # variable for user input
        message = ""
        Encrypt = ""

        # for asking user input until it is valid
        while True:
            # asking message/input from the user
            print("Enter the message you want to encrypt:")
            msg = input("-> ")
            # advance_loding_animation()

            # checking it the input are empty or equals to 1
            if msg == "" or len(msg) == 1:
                print("Invalid input. Please Enter your message again.")
            else:
                message = msg
                # if valid exiting from the loop
                break
            
        # main
        for word in message.split():

            # if word has 1 letter in it
            if len(word) == 1:
                Encrypt = Encrypt + word
                Encrypt = Encrypt + " "

            # if word has 2 letters:
            elif len(word) == 2:
                chars = list(word)
                chars[0], chars[1] = chars[1], chars[0]
                for char in chars:
                    Encrypt = Encrypt + char
                Encrypt = Encrypt + " "
                    
            # if word hase more than 2 letters:
            else:
                random_letter = random.choices(string.ascii_letters, k=3)
                temp = ""
                for letter in word:
                    temp = letter + temp
                str_random = "".join(random_letter)
                temp = str_random + temp
                Encrypt = Encrypt + temp
                Encrypt = Encrypt + " "
            
        # Returns the Encrypted message. 
        return Encrypt

    # handeling all the error ocurred
    except Exception as e:
        print("Something went wrong during process.", e)
        traceback.print_exc()

    # displaying encrypted messaege
    finally:
        print_line()
        print("Your Encrypted message is:", Encrypt if 'Encrypt' in locals() else "")
        print_line()


def decrypt():
    
    try:
        # variables
        Encrypt_msg = ""
        Decrypt_msg = ""

        while True:
            # asking encrpted message from user
            print("Enter encrypt message your want to decrypt:")
            msg = input("-> ")
            # advance_loding_animation()

            # checking if the input is empty or not
            if msg == "":
                print("It cannot be empty. Please fill up the message.")
            else:
                Encrypt_msg = msg
                break
        
        # seprating sentence
        for word in Encrypt_msg.split():
            
            # if length of word is 1
            if len(word) == 1:
                Decrypt_msg = Decrypt_msg + word
                Decrypt_msg = Decrypt_msg + " "

            # if length of word is 2
            elif len(word) == 2:
                chars = list(word)
                chars[0], chars[1] = chars[1], chars[0]
                for char in chars:
                    Decrypt_msg = Decrypt_msg + char
                Decrypt_msg += " " 

            # if its length is more than 2
            else:
                # removing the first 3 decoy letter
                temp = ""
                word = list(word)
                word = word[3:len(word)]

                # reversing the word
                for char in word:
                    temp = char + temp
                temp += " "
                Decrypt_msg += temp
        
        # returning the decrypte message
        return Decrypt_msg
    
    # handeling all the error ocurred
    except Exception as e:
        print("Something went wrong.", e)
        traceback.print_exc()
        
    # displaying decrypted messaege
    finally:
        print_line()
        print("Your Decrypt message is:", Decrypt_msg if 'Decrypt_msg' in locals() else "")
        print_line()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#  main:
try:
    
    

    while True:
        print("\n " + "-"*150)
        print(f"| {'Enter between 1 to 3:':<149}|")
        print("|"+"-"*150 + "|")
        print(f"| {'1. Encrypt message':<149}|")
        print(f"| {'2. Decrypt message':<149}|")
        print(f"| {'3. Exit':<149}|")
        print(" "+"-"*150 + "")
        print("Enter your choice: ")
        choice = input("-> ")
        print()

        if choice == "1":
            # # advance_loding_animation()
            message = encrypt()
            
        elif choice == "2":
            # # advance_loding_animation()
            message = decrypt()
            
        elif choice == "3":
            # advance_loding_animation()
            print("Exit sucessfully")
            break
        else:   
            print("Invalid input. Please try again. ")


except Exception as e:
    print("Something went wrong.", e)