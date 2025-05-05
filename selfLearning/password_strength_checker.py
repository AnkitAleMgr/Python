'''
password_strength_checker is a program build by using python. It check the password, analize it, give suggesion:
Objective:
1. To make secure password
2. To learn more about python and it nature
3. To self-improvement
4. To learn proper and organized way of coding

Feature:
1. should check for passwork strenth
2. Should notify them and suggest them
3. Should also reank them as a bonus
4. it should ask user more input

road map:
1. it should take input from the user, if it is empty it should notify the user
2. if should check if it has al least 8 digit or not, if yes +1 on password_secutiry_level
3. it should check it it has alphabates in it or not if yes +1 on level
4. it should check if it has number mixer or not, if yes +1 on level
5. if there are aplhabates it should check if it has both lower and upper case letter, if yes +1
6. it should check if it has special charecters, if yes +1
7. it should return the password_security_level
 

'''
import re
# from simple_calculator
# import simple_calculator

def main():
    password = value()
    a , b =checker_operation(password)
    print(a, b)
    special_charecter_checker(a,b)
    

def value():
    value = input("\nEnter a password you want to check: ")
    while value == "":
        value = input("\nPlease input the password: ")
    return value


def special_charecter_checker(a, b):
    password = a
    password_security_level= b

    print("Checking if your password has special charecter or not")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        password_security_level +=1
        print("Your password contain special charecter.")
    else:
        print("Your password doesn;t contain special charecter")
        new_password = changing_password_operation(password)
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]",new_password):
            password_security_level += 1



def checker_operation(password):
    password_security_level = 0
    print("Checking if your password is long or not")
    if len(password) >= 8:
        print("Your password length is good enough.")
        password = changing_password_operation(password)  # Call only once
        if len(password) >= 8:  # Use the updated password
            password_security_level += 1
    elif len(password) >= 15:
        print("Your password length is good")
        password = changing_password_operation(password)  # Call only once
        if len(password) >= 8:  # Use the updated password
            password_security_level += 1
    else:
        print("Your password length is small")
        password = changing_password_operation(password)  # Call only once
        if len(password) >= 8:  # Use the updated password
            password_security_level += 1
    return password, password_security_level

def changing_password_operation(password):
    a = True
    while a:
        changing_password_value = input("\nDo you want to change you password size: ")
        if changing_password_value.lower().strip() == "yes":
            password = repassword_checker(password)
        elif changing_password_value.lower().strip() == "no":
            print("exiting...")
            a = False
            return password
        else:
            print("Invalid input")

def repassword_checker(password):
    a = True
    while a:
        new_password = input("Please enter new password: ")
        if password == new_password:
            print("previou and new password is same.")
        elif password == "":
            print("It cannot be empty.")
        else:
            a = False

    return new_password  

main()