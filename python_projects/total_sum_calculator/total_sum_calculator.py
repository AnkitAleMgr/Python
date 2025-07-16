# question
# making a calculator that sun the products amounts and calculator sum of products. and when press entry display total price

total_price = 0
EXIT_KEYWORD = {"q", "quit", "exit", "e", ""}


print("-"*148)
amount = input("Enter the price of product: ")
while amount not in EXIT_KEYWORD:
    try:
        amount = int(amount)
    except:
        print("Input amount cannot be converter number")
        amount = input("Enter the price of product: ")
        continue
    total_price += amount
    
    amount = input("Enter the price of product: ")
print("-"*148)
print("Total price:",total_price)
print("-"*148)

# print("-"* 148)
# while True:
#     amount = input("Enter the price of product: ")
#     if amount in EXIT_KEYWORD:
#         print("Caculating total price..")
#         print("-"* 148)
#         print("Total price: ", total_price)
#         print("-"* 148)
#         break
#     else:
#         try:
#             amount = int(amount)
#         except:
#             print("Amount cannot be converted into number.")
#         total_price += amount
