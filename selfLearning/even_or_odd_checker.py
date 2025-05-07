
def odd_even():

    # a = ""
    value = int(user_Input)

    if value % 2:
        a = "\nEven"
    else:
        a = "\nOdd"

    return a

a = True

while a:
    user_Input = input("Enter a number To find if it is odd or even: \n")

    
    if user_Input == "": 
        print("\nYou cannot put an empty value")
        # user_Input = input("Enter a number To find if it is odd or even: \n")

    elif not user_Input.isdigit():
        print("\nIt should be digit only")
        # user_Input = input("Enter a number To find if it is odd or even: \n")

    else:
        print(odd_even())
        c = True
        
        while c:
            again_check = input("Do you want to check another numebr (yes/no): \n")

            if again_check.lower() == "yes":
                c = False

            elif again_check.lower() == "no":
                a = False
                c = False

            else:
                print("Invalid input")
