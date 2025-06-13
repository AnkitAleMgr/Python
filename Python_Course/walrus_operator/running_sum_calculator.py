# You’ll use the walrus operator to:
# Assign the input to a variable
# Calculate the running sum while checking if it's still under 100

def main():
    # variable
    total:int = 0

    # checking if it is below 100 or not
    while ( total := (value := int(input("Enter a number: ")) + total)) < 99 :
        print(total)
        

# entry point
if __name__ == "__main__":
    main()