class Coffee:

    def __init__(self, name : str , size : str, price : float) -> None:
        self.name = name
        self.size = size
        self.price = float(price)
    
    def display_info(self):
        print(f"Coffee Name: {self.name}")
        print(f"Size: {self.size}")
        print(f"Price: ${self.price:.2f}")

class Customer:
    
    def __init__(self, name : str) -> None:
        self.name = name 
        self.order = []

    def place_order(self, coffee : Coffee)-> None:
        self.order.append(coffee)
        print(f"{coffee.name} has been added to {self.name}'s order.")
    
    def view_order(self) -> None:
        if not self.order:
            print("No orders placed yet.")
        else:
            print(f"Order of {self.name}")
            for index,item in enumerate(self.order, start=1):
                print(f"{index}) {item.name} - {item.size} - ${item.price:.2f}")

if __name__ == "__main__":
    
    # creating at least 2 coffee objects
    coffee1 = Coffee("Espresso", "Small", 2.50)
    coffee2 = Coffee("Latte", "Medium", 3.75)

    # creating a customer object
    customer1 = Customer("Ankit")
    
    # displaying empty customer order
    customer1.view_order()

    # placing orders
    customer1.place_order(coffee= coffee1)
    customer1.place_order(coffee= coffee2)
    
    customer1.view_order()