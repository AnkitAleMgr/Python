from abc import ABC, abstractmethod

class MenuItem(ABC):
    def __init__(self, name, price, description=''):
        self.name = name
        self.price = price
        self.description = description

    @abstractmethod
    def get_category(self):
        pass

    def __str__(self):
        return f"{self.name} (${self.price:.2f}) - {self.description}"

class Drink(MenuItem):
    def get_category(self):
        return "Drink"

class MainCourse(MenuItem):
    def get_category(self):
        return "Main Course"

class Dessert(MenuItem):
    def get_category(self):
        return "Dessert"

class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []  # list of tuples (MenuItem, quantity)

    def add_item(self, menu_item, quantity=1):
        self.items.append((menu_item, quantity))

    def total_price(self):
        return sum(item.price * qty for item, qty in self.items)

    def __str__(self):
        order_details = '\n'.join([f"{item.name} x{qty} - ${item.price * qty:.2f}" for item, qty in self.items])
        return f"Order for {self.customer.name}:\n{order_details}\nTotal: ${self.total_price():.2f}"

class Customer:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = []
        self.orders = []

    def add_menu_item(self, item):
        self.menu.append(item)

    def show_menu(self):
        print(f"Menu for {self.name}:")
        for item in self.menu:
            print(f"{item.get_category()} - {item}")

    def take_order(self, customer, order):
        self.orders.append(order)
        customer.place_order(order)
        print(f"Order received for {customer.name}")

# Example usage:

if __name__ == "__main__":
    restaurant = Restaurant("Tasty Food Place")

    # Add items to menu
    restaurant.add_menu_item(Drink("Coke", 1.99, "Refreshing cola"))
    restaurant.add_menu_item(MainCourse("Burger", 5.99, "Juicy beef burger"))
    restaurant.add_menu_item(Dessert("Ice Cream", 3.49, "Vanilla flavor"))

    restaurant.show_menu()

    # Customer and order
    cust = Customer("Alice", "alice@example.com")
    order = Order(cust)
    order.add_item(restaurant.menu[0], 2)  # 2 Cokes
    order.add_item(restaurant.menu[1])     # 1 Burger

    restaurant.take_order(cust, order)

    print(order)
