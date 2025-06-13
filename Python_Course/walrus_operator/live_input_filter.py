# Build a small script that:
# Asks the user for input repeatedly.
# Immediately checks if the input contains a specific keyword (like "python").
# Prints it only if the condition is met.
# Exits when the user types "q" or "quit".

while (word := input("Enter a word: ")) not in ["q", "quit"]:
    if "python" in word.lower():
        print(f"found python in {word}")