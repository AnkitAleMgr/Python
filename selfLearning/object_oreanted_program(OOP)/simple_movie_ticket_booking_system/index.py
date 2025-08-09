class Movie():

    def __init__(self, title : str, duration : int, price : float) -> None:
        self.title = title.capitalize()
        self.duration = int(duration)
        self.price = float(price)

    def display_info(self) -> None:
        print("Title",self.title)
        print("Duration",self.duration)
        print("Price $",self.price)
        return ""

class Customer():

    def __init__(self, name : str)-> None:
        self.name = name.capitalize()
        self.tickets = []

    def book_ticket(self, ticket : Movie) -> None:
        self.tickets.append(ticket)
        print(f"{ticket.title} has been booked for {self.name}")

    def view_ticket(self):
        if self.tickets:
            print(f"{self.name} booked ticket:")
            for index, ticked in enumerate(self.tickets, start= 1):
                ticked.display_info()


if __name__ == "__main__":
    
    # creaing the at least 2 object of movie
    thor = Movie(title= "Thor", duration= 100, price= 20)
    spider_man = Movie(title="spider man", duration= 120, price= 30)

    # creaing a customer
    ankit = Customer(name= "ankit")
    
    ankit.book_ticket(thor)
    ankit.book_ticket(spider_man)

    ankit.view_ticket()


        