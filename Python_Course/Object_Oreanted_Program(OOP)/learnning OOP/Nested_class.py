class Laptop:

    class Battery:
        def __init__(self, battery) -> None:
            self.battery = battery + "V"

        def show_battery_detail(self):
            return self.battery
            
            
    
    def __init__(self, name : str, price : int, battery : int) -> None:
        self.name = name
        self.price = price
        self.battery = self.Battery(battery)

    def detail(self):
        return self.name, self.price, self.Battery.show_battery_detail
    