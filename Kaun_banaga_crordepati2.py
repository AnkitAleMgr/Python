a = questions = [
    ["What is the capital of France?", "Berlin", "London", "Paris", "Rome", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["Who wrote 'Romeo and Juliet'?", "Shakespeare", "Tolstoy", "Hemingway", "Dickens", 1],
    ["What is the largest mammal?", "Elephant", "Whale", "Giraffe", "Hippo", 2],
    ["Which gas do plants absorb?", "Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen", 2],
    ["How many continents are there?", "5", "6", "7", "8", 3],
    ["Which ocean is the deepest?", "Atlantic", "Indian", "Pacific", "Arctic", 3],
    ["Which country hosted the 2020 Olympics?", "China", "Japan", "Brazil", "USA", 2],
    ["Which instrument has keys, pedals and strings?", "Guitar", "Drums", "Piano", "Violin", 3],
    ["Which element has the chemical symbol 'O'?", "Gold", "Oxygen", "Osmium", "Zinc", 2]
]

price = 0

for i in a:
    question = i
    a = 0
    
    
    print(f"{question[a]}\noption {question[1:-1]}:")
    choice = input("→ ")
    
    if choice.title().strip() == question[question[-1]].title().strip():
        if price == 0:
            price += 1000
            print("-"*100)
            print(f"Correct answer. your current price is {price}")
            print("-"*100 + "\n")
        else:
            price *= 2
            print("-"*100)
            print(f"correct answer. your current price is {price}")
            print("-"*100 + "\n")
            
    else:
        print("-"*100)
        print("Incorrect answer.")
        print("-"*100 + "\n")

print("Your final price is {}".format(price))
    