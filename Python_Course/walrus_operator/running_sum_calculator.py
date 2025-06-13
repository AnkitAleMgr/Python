# You’ll use the walrus operator to:
# Assign the input to a variable
# Calculate the running sum while checking if it's still under 100

total = 0

while ( total := (value := int(input("Enter a number: ")) + total)) < 99 :
    print(total)
