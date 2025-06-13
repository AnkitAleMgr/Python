import os

foods = list()

while (food := input("Enter a food: ")) != "exit":
    foods.append(food)
    print(f"{food} has been add in {foods}")

os.system("clear")
print(f'{(str_food := ", ".join(foods))}')
